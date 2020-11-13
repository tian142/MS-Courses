# API documentation: https://openweathermap.org/current
import requests
from pprint import PrettyPrinter
from datetime import datetime

pp = PrettyPrinter(indent=4)

url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    # TODO 1: Add your own API key by following these instructions: https://openweathermap.org/appid
    'appid': '7e247499e6bbed93c3bd35baf2018838',
    'q': 'San Francisco',
    'units': 'imperial'
}

response = requests.get(url, params=params)
response_json = response.json()
pp.pprint(response_json)

# TODO 2: get the temperature in degrees F from response
# HINT: Look at the JSON that is being printed to figure out how!
temperature = response_json["main"]["temp"]
print(f'\n\nIt is {temperature} degrees Fahrenheit today.')

# TODO 3: replace this with the weather's 'description' field, e.g. 'mostly sunny'
description = response_json["weather"][0]["description"]
print(f'The weather is {description} today.')

risetime = response_json["sys"]['sunrise']
settime = response_json["sys"]['sunset']

printRise = datetime.fromtimestamp(risetime)
printSet = datetime.fromtimestamp(settime)

print(f'rise: {printRise}. set: {printSet}')


# Stretch challenge: Get the sunrise/sunset and convert to time of day
# (Convert epoch time into time of day - hour:minute)
