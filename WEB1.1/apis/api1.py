# Run the program by pressing "Run" to see the results of the API call.

# API Documentation: http://www.icndb.com/api/

import requests
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)

params = {
    "limitTo": "nerdy",
}
result = requests.get(
    "http://api.icndb.com/jokes/random",
    params=params)
joke_json = result.json()
pp.pprint(joke_json)

# TODO 1: Use the API documentation (linked above) to learn how to change the first and last name of the target of the joke. (E.g. instead of "Chuck Norris", the API will send back a joke about "Ada Lovelace", or whichever first/last name is specified.)
# Then, make another API request to request a joke with your first and last name.

pp = PrettyPrinter(indent=4)

params = {
    "limitTo": "nerdy",
    "firstName": "Sam",
    "lastName": "Joe"
}
result = requests.get(
    "http://api.icndb.com/jokes/random",
    params=params)
joke_json = result.json()
pp.pprint(joke_json)

# TODO 2: Use the documentation to learn how to request the total number of jokes in the database. Then, make a request to get the total number of jokes.

pp = PrettyPrinter(indent=4)

params = {
    "limitTo": "nerdy",
}
result = requests.get(
    "http://api.icndb.com/jokes/random/5",
    params=params)
joke_json = result.json()
pp.pprint(joke_json)

# TODO 3: Use the documentation to learn how to request the joke with a specific ID. Then, request joke #463 (or any other number you like).

pp = PrettyPrinter(indent=4)

params = {
    "limitTo": "nerdy",
}
result = requests.get(
    "http://api.icndb.com/jokes/463",
    params=params)
joke_json = result.json()
pp.pprint(joke_json)


# STRETCH CHALLENGE: Use Python dictionary syntax to extract just the joke text, and print it to the console instead of printing the entire response.

pp = PrettyPrinter(indent=4)

params = {
    "limitTo": "nerdy",
}
result = requests.get(
    "http://api.icndb.com/jokes/463",
    params=params)

joke_json = result.json()

print(joke_json['value']['joke'])
print(joke_json.get('value', {}).get('joke'))
