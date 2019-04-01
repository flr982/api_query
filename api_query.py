# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 23:53:19 2019

@author: Florian
"""

#!/bin/python3.6

api_key="689136764b63eec9cdda8c472bfb4ade"
openweathermap_api_key="fea5818d9b0df04a9ed640796a31b06e"
import urllib.request
import json
import mysql.connector
from datetime import datetime

def owm(query):
    api_key = openweathermap_api_key
    url = "https://api.openweathermap.org/data/2.5/find?q="
    location = query.replace(" ", "%20")
    final_url = url + location + "&units=metric&APPID=" + api_key
    json_obj = urllib.request.urlopen(final_url)
    data = json.load(json_obj)
    unix_time = data["list"][0]["dt"]
    time = datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')
    city = data["list"][0]["name"]
    country =  data["list"][0]["sys"]["country"]
    temp = str(data["list"][0]["main"]["temp"])
    weather = data["list"][0]["weather"][0]["main"]
    return(city, country, temp + "C", weather, time)

def print_owm(query):
    print(owm(query))
