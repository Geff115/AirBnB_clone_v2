#!/usr/bin/python3
"""
This script starts a Flask web application
"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_text(text="is cool"):
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<n>', strict_slashes=False)
def number_n(n):
    n = int(n)
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<n>', strict_slashes=False)
def number_template_n(n):
    try:
        n = int(n)
    except ValueError:
        return "n cannot be converted to an integer"
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
