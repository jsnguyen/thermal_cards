#!/usr/bin/python3

import requests
import datetime
import dateutil.parser

with open('coords.txt','r') as f:
    lat,lon = [float(el) for el in f.readline().split(',')]
coord_str = str(lat)+','+str(lon)

weather_gov_url = 'https://api.weather.gov/points/'
wgur = requests.get(weather_gov_url+coord_str)

json_response = wgur.json()

forecast_url = (json_response['properties']['forecast'])

fur = requests.get(forecast_url)

weather_now = (fur.json()['properties']['periods'][0])
today = datetime.datetime.now()

print(today.strftime('%B %d, %Y\nPrint Time: %I:%M:%S %p'))
print('-------------------------')
#print(weather_now['temperature'],weather_now['temperatureUnit'])
#print(weather_now['windSpeed'],weather_now['windDirection'])
print(weather_now['detailedForecast'])

sunrise_sunset_url = 'https://api.sunrise-sunset.org/json?lat='+str(lat)+'&lng='+str(lon)+'&date='+today.strftime('%Y-%m-%d')+'&formatted=0'

ssur = requests.get(sunrise_sunset_url)

json_response = ssur.json()

UTC_to_PST_offset = datetime.timedelta(hours=-7)
sunrise = dateutil.parser.parse(json_response['results']['sunrise'])+UTC_to_PST_offset
sunset  = dateutil.parser.parse(json_response['results']['sunset'])+UTC_to_PST_offset

sunrise_str = sunrise.strftime('%I:%M:%S %p')
sunset_str = sunset.strftime('%I:%M:%S %p')
print('-------------------------')
print('Sunrise:',sunrise_str)
print('Sunset:',sunset_str)
print()
print()
print()
print()
