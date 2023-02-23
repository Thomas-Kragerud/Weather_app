from datetime import datetime
import os
import pytz
import requests
import math

API_KEY = "c50ca96607d90d05b45870201c4b06b3"
#API_KEY = os.environ.get('WEATHER_API_KEY')  # This only works when running in same terminal. i.e. python3 weather.py
API_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}'


def query_api(city):
    try:
        print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data
