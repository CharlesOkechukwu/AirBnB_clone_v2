#!/usr/bin/python3
"""Module to start Flask application
and display HBnB static"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Function to display a string
    Hello, HBNB"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
