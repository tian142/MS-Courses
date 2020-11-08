from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello')
def homepage():
    return render_template('hello.html')


@app.route('/profile/<user>')
def profile(user):
    return "hello " + user


@app.route('/triple/<words>')
def triple_word(words):

    # return f"{words} {words} {words}"
    return ((words + ' ')*3).strip()


if __name__ == '__main__':
    app.run(debug=True)
