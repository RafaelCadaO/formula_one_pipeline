import os
from dotenv import load_dotenv, dotenv_values
import requests
import psycopg2
import time
import logging
import sys
from datetime import datetime


class Main:

    def __init__(self):
        print(f'--> START <--')
        self.Session = None
        self.sql_cursor = None
        self.start = time.time()
        self.file_main_path = sys.argv[0]
        self.name_file_main_path = self.file_main_path.split('/')[-1].replace('.py', '')
        self.env_load = load_dotenv()
        self.logger = self.setup_logger()

    def __del__(self):
        self.end = time.time()
        print('Execution duration:' + str(self.start - self.end) + 'sec')

    def setup_logger(self):
        execution_date = datetime.now().strftime('%Y-%m-%d %H-%M')
        logs_path = f'/Users/macbookpro/dev/f1/pythonProject/logs'
        log_file_name = f'{logs_path}/{execution_date}_{self.name_file_main_path}.log'
        logging.basicConfig(filename=log_file_name, level=logging.INFO,
                            filemode='w', datefmt='%Y-%m-%d %H-%M')
        return logging.getLogger(__name__)

    def sql_connection(self, procedure_name=None, csv_path=None):
        conn_params = {
            'dbname': os.getenv('dbname'),
            'user': os.getenv('user_db'),
            'password': os.getenv('pass_db'),
            'host': os.getenv('host_name'),
            'port': os.getenv('port')
        }
        try:
            conn = psycopg2.connect(**conn_params)
            print("Successful connection to PostgresSQL")
            self.logger.info("Successful connection to PostgresSQL")

            self.sql_cursor = conn.cursor()

            call_command = f"CALL {procedure_name}(%s)"
            self.sql_cursor.execute(call_command, (csv_path,))
            conn.commit()
            self.sql_cursor.close()
            conn.close()

            return self.sql_cursor

        except Exception as e:

            print(f"Error at execution of {procedure_name}: {e}")
            self.logger.info(f"Error at execution of {procedure_name}: {e}")


class RequestsClass(Main):

    def __init__(self):
        super().__init__()
        self.session = requests.Session()

    def __del__(self):
        return super().__del__()

    def make_request(self, https, type_request='get', params=None, data=None, json=None, files=None):
        for attempt in range(0, 5):
            try:
                if type_request == 'get':
                    response = self.session.get(https, params=params)
                elif type_request == 'post':
                    response = self.session.post(https, data=data, json=json, files=files, stream=True)
                else:
                    raise ValueError('Method not valid, use GET or POST')
                response.raise_for_status()
                return response
            except requests.exceptions.RequestException as e:
                if attempt >= 4:
                    raise ValueError(e)
                print(f'Error in request to {https}: {e}')
                self.logger.info(f'Error in request to {https}: {e}')