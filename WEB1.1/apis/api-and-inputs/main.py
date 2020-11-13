# API Documentation: http://www.icndb.com/api/

from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    """Show the homepage."""
    return render_template('index.html')


@app.route('/joke_results')
def joke_results():
    """Show user a joke."""
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    gender = request.args.get('gender')

    params = {
        "limitTo": "nerdy",
        "firstName": first_name,
        "lastName": last_name
    }

    response = requests.get("http://api.icndb.com/jokes/random", params=params)
    joke_json = response.json()
    joke_text = joke_json["value"]["joke"]

    if gender == 'male':
        joke_text.replace("she", "he")
        joke_text.replace("her", "him")
    elif gender == 'female':
        joke_text.replace("he", "she")
        joke_text.replace("him", "her")
    else:
        joke_text.replace("he", "they")
        joke_text.replace("him", "them")
        joke_text.replace("she", "they")
        joke_text.replace("her", "them")

    return f"Here's your joke! <br><br> {joke_text}"


# STRETCH CHALLENGE: Modify `home.html` to have a drop-down (or input box, radio buttons, etc) for the user's gender. Then, before returning the joke text, replace all instances of 'he', 'him', etc with the appropriate gendered pronoun.
# HINT: Use the Python string replace function: https://www.tutorialspoint.com/python/string_replace.htm
app.run('0.0.0.0', debug=True)
