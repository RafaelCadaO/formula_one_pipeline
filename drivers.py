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


def get_drivers(main_code):
    https = ENTITIES_F1[0]['url']
    drivers = main_code.make_request(https=https, type_request='get', params={"session_key": "latest"})
    formated = drivers.json()
    logging.info(f"peticion exitosa {https}")
    return formated


def stream_data(main_code):
    pathDest = f'/Users/macbookpro/dev/f1/pythonProject/data/'
    pathDrivers = f'{pathDest}Drivers.csv'
    drivers = get_drivers(main_code)
    df_drivers = pandas.DataFrame(drivers)

    df_drivers.to_csv(pathDrivers, encoding='utf-8', index=False, header=True, sep='\t')
    time.sleep(5)

    procedure_name = f'public.load_driver_data_from_csv'
    csv_path = pathDrivers
    main_code.sql_connection(procedure_name=procedure_name, csv_path=csv_path)
    print(f'-->End<--')
    main_code.logger.info(f'-->End<--')


if __name__ == "__main__":

    main_code = RequestsClass()
    main_code.logger.info(f'-->Start<--')
    stream_data(main_code)
