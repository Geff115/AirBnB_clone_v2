#!/usr/bin/python3
"""
This script starts a Flask web application listening
on port 5000
"""


from . import app


@app.route('/', strict_slashes=False)
def hello():
    """
    This function returns Hello HBNB!
    """

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function returns HBNB
    """

    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)