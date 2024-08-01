from Main.Main import RequestsClass
import pandas
import logging
import time

ENTITIES_F1 = [
    {"entity": "drivers_f1", "url": "https://api.openf1.org/v1/drivers"},
    {"entity": "locations_f1", "url": "https://api.openf1.org/v1/locations"},
    {"entity": "sessions_f1", "url": "https://api.openf1.org/v1/sessions"},
    {"entity": "intervals_f1", "url": "https://api.openf1.org/v1/intervals"},
    {"entity": "car_data_f1", "url": "https://api.openf1.org/v1/car_data"},
    {"entity": "laps_f1", "url": "https://api.openf1.org/v1/laps"},
    {"entity": "meetings_f1", "url": "https://api.openf1.org/v1/meetings"},
    {"entity": "pit_f1", "url": "https://api.openf1.org/v1/pit"},
    {"entity": "position_f1", "url": "https://api.openf1.org/v1/position"},
    {"entity": "stints_f1", "url": "https://api.openf1.org/v1/stints"},
    {"entity": "weather_f1", "url": "https://api.openf1.org/v1/weather"}
]


def get_sessions(main_code):
    https = ENTITIES_F1[2]['url']
    sessions = main_code.make_request(https=https, type_request='get', params={"session_key": "latest"})
    formated = sessions.json()
    logging.info(f"peticion exitosa {https}")
    return formated


def stream_data(main_code):
    """

    :param main_code:
    :return:
    """
    pathDest = f'/Users/macbookpro/dev/f1/pythonProject/data/'
    pathSessions = f'{pathDest}Sessions.csv'
    sessions = get_sessions(main_code)
    df_sessions = pandas.DataFrame(sessions)


    df_sessions.to_csv(pathSessions, encoding='utf-8', index=False, header=True, sep='\t')
    time.sleep(5)

    procedure_name = f'public.load_session_data_from_csv'
    csv_path = pathSessions
    main_code.sql_connection(procedure_name=procedure_name, csv_path=csv_path)


if __name__ == "__main__":

    main_code = RequestsClass()
    logging.basicConfig(level=logging.DEBUG)
    stream_data(main_code)
