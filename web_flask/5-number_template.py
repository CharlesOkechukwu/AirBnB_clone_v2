#!/usr/bin/python3
"""Module to start Flask application
and display HBnB static and Hello HBNB static"""
from flask import Flask
from flask import render_template


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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_url(text='is cool'):
    """print string when python is added to url
    with a default value of 'is cool'
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """print a string only if n is an integer"""
    if type(n) is int:
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def temp(n):
    """display a html number template if n is
    an integer"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
