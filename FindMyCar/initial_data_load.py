# from django.conf import settings
import VehicList.settings as settings
import os
import sys
import mysql.connector as mc
import pandas as pd
from sqlalchemy import create_engine

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))

zip_db = 'findmycar_zipinfo'
vehicle_db = 'findmycar_vehicle_listings'
dealer_db = 'findmycar_dealers'

zip_charSet = 'utf8'
vehicle_charSet = 'utf8'
dealer_charSet = 'utf8'

dbname = settings.DATABASES['default']['NAME']
user = settings.DATABASES['default']['USER']
password = settings.DATABASES['default']['PASSWORD']
host = settings.DATABASES['default']['HOST']
port = 3360


zip_Info = pd.read_csv(settings.ZIP_INFO_PATH,
                       delimiter=',', names=('zip_code', 'state_code', 'latitude', 'longitude', 'city', 'state'))
# zip_info = zip_info.applymap(prune)
listings = pd.read_csv(
    settings.VEHICLE_INFO_PATH, encoding='raw_unicode_escape', engine='python', names=('vehicle_live_id', 'vin', 'stock', 'make', 'model', 'trim', 'year',
                                                                                       'amenities', 'price', 'miles', 'exterior', 'description', 'certified',
                                                                                       'transmission', 'body_type', 'speeds', 'doors', 'cylinders', 'engine',
                                                                                       'displacement', 'zip_code', 'phone', 'imagefile', 'dealer_number', 'Distance'), skiprows=1)

# None value column removed during Data Pruning
listings.drop(['speeds', 'phone'], inplace=True, axis=1)

dealers = pd.read_csv(settings.DEALER_INFO_PATH,
                      encoding='unicode_escape', engine='python', names=('dealer_number', 'dealer_name', 'dealer_address'), dtype={'dealer_number': str, 'dealer_name': str, 'dealer_address': str})


class load_Data():
    def __init__(self, user, password, dbname, host, port):
        self.user = user
        self.password = password
        self.dbname = dbname
        self.host = host
        self.port = port

    def loadData(self, charSet, table, dataFrame):
        connection_string = f'mysql+mysqldb://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}?charset={charSet}'
        con_engine = create_engine(
            connection_string, pool_recycle=3600, pool_pre_ping=True, echo=False)
        dataFrame.to_sql(f'{table}', con=con_engine,
                         if_exists='append', index=False)
        print(F"{dataFrame} injected Successfully")


if __name__ == '__main__':

    zip_load = load_Data(user, password, dbname, host, port)
    vehicle_load = load_Data(user, password, dbname, host, port)
    dealer_load = load_Data(user, password, dbname, host, port)

    zip_load.loadData(zip_charSet, zip_db, zip_Info)
    vehicle_load.loadData(vehicle_charSet, vehicle_db, listings)
    dealer_load.loadData(dealer_charSet, dealer_db, dealers)
