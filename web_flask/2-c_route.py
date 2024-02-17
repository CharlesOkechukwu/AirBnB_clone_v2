#!/usr/bin/python3
"""Module to start Flask application
and display HBnB static and Hello HBNB static"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Function to display a string
    Hello, HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function to display only hbnb string
    HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
    """print string in url and repl;ace underscores
    with spaces"""
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
