from django.http.response import HttpResponse
from django.shortcuts import render
import pandas as pd
# import os
from geopy import distance
import numpy as np
import time
# import multiprocessing
import mysql.connector as mc
# from django.conf import settings
from . import initial_data_load as data


def display_cars(request):
    pin = request.POST["pinCode"]
    dist = int(request.POST["distance"])
    conn = mc.connect(user='root', password='Smarter51',
                      host='localhost', database='findmycar')
    cursor = conn.cursor()
    # Reuse the Pre-Data load csv loads and determine lat and long of the user provided zip code
    lat = float(
        data.zip_Info.loc[data.zip_Info["zip_code"] == pin]["latitude"].values[0])
    lon = float(
        data.zip_Info.loc[data.zip_Info["zip_code"] == pin]["longitude"].values[0])
    # Fetch all the locations which is the required distance vicinity
    distance_query = f"select zip_code,(3959 * acos(cos(radians({lat})) * cos(radians(findmycar_zipinfo.latitude)) * cos(radians(findmycar_zipinfo.longitude) - radians({lon})) + sin(radians({lat})) * sin(radians(findmycar_zipinfo.latitude)))) AS distance from findmycar_zipinfo having distance < {dist} ORDER BY distance;"
    cursor.execute(distance_query, multi=True)
    zip_values = pd.DataFrame(cursor.fetchall())

    # use this Python Data Structuere to reduce the Query complexity and DB proceessing time as well as performance
    # Fetch all the required fields in one query to reduce the number of DB hits
    details_query = f"select detail.year, detail.make, detail.model, detail.price, detail.dealer_name, findmycar_zipinfo.state, findmycar_zipinfo.city, findmycar_zipinfo.zip_code from (select final_list.year, final_list.make, final_list.model, final_list.price, findmycar_dealers.dealer_name, final_list.zip_code , final_list.vin from (select  year, make, model, price, dealer_number, zip_code, vin from findmycar_vehicle_listings where zip_code in {tuple(zip_values[0])}) as final_list INNER JOIN findmycar_dealers ON final_list.dealer_number = findmycar_dealers.dealer_number group by final_list.vin) as detail INNER JOIN findmycar_zipinfo ON detail.zip_code = findmycar_zipinfo.zip_code group by detail.vin;"
    cursor.execute(details_query)
    details = pd.DataFrame(cursor.fetchall())
    print(len(details.values))
    details.columns = ['Year', 'Make', 'Model', 'Price',
                       'Dealer', 'State', 'City', 'Zip Code']
    conn.close()
    return render(request, 'test.html', {'details': details})


def finder_home(request):
    return render(request, 'finder_home.html')
