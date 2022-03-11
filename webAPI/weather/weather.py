#!/usr/bin/env python3
"""simple script to turn a dictionary of weather forecast related values
   into an English description of the forecasr"""

import requests


def get_data():
    """Use requests to get weather data"""
    try:
        # response = requests.get(
        #    'https://www.metaweather.com/api/location/2455920')
        r = requests.get(
            'https://www.metaweather.com/api/location/2459115')
    except requests.exceptions.ConnectionError:
        print("Unable to connect to the server")
    if r.status_code != 200:
        print("oops, something went wrong \n"
                  f"HTTP response = {r.status_code}")
    return r


r = get_data()
weather_data = r.json()
for day in weather_data['consolidated_weather']:
    date = day['applicable_date']
    state = day['weather_state_name']
    temp = day['the_temp']
    print(f"The weather for {date} will be {state} with a temperature of {temp:.2f} degrees.")
