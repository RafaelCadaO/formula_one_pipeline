import os
from dotenv import load_dotenv, dotenv_values
import requests
import psycopg2
import time


class Main:

    def __init__(self):
        print(f'--> START <--')
        self.Session = None
        self.sql_cursor = None
        self.start = time.time()
        self.env_load = load_dotenv()

    def __del__(self):
        self.end = time.time()
        print('Execution duration:' + str(self.start - self.end) + 'sec')

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
            print("Conexión exitosa a PostgreSQL")

            self.sql_cursor = conn.cursor()

            # Llamar al procedimiento almacenado
            call_command = f"CALL {procedure_name}(%s)"
            self.sql_cursor.execute(call_command, (csv_path,))
            conn.commit()
            self.sql_cursor.close()
            conn.close()

            return self.sql_cursor

        except Exception as e:

            print(f"Error al ejecutar el procedimiento {procedure_name}: {e}")


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
