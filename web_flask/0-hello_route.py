#!/usr/bin/python3
"""
This script starts a Flask web application listening on port 5000
"""

from . import app


@app.route('/', strict_slashes=False)
def hello():
    """
    This function returns Hello HBNB!
    """

    return "Hello HBNB!"


if __name__ == "__main__":
    """
    Ensuring that the application runs on port 5000
    """

    app.run(host='0.0.0.0', port=5000)
