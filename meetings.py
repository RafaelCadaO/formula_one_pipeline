from Main.Main import RequestsClass
import pandas
import logging
import time
from datetime import date

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


def get_meetings(main_code):
    https = ENTITIES_F1[6]['url']
    meetings = main_code.make_request(https=https, type_request='get', params={"year": date.today().year, "country_name": "Belgium"})
    formated = meetings.json()
    logging.info(f"peticion exitosa {https}")
    return formated


def stream_data(main_code):
    pathDest = f'/Users/macbookpro/dev/f1/pythonProject/data/'
    pathMeetings = f'{pathDest}Meetings.csv'
    meetings = get_meetings(main_code)
    df_meetings = pandas.DataFrame(meetings)
    print(df_meetings)
    df_meetings.to_csv(pathMeetings, encoding='utf-8', index=False, header=True, sep='\t')
    time.sleep(5)

    procedure_name = f'public.load_session_data_from_csv'
    csv_path = pathMeetings
    #main_code.sql_connection(procedure_name=procedure_name, csv_path=csv_path)


if __name__ == "__main__":

    main_code = RequestsClass()
    logging.basicConfig(level=logging.DEBUG)
    stream_data(main_code)
