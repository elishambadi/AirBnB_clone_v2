#!/usr/bin/python3
"""
   Starts a flask web app
"""
from flask import Flask, escape, abort
app = Flask('__main__')


@app.route('/', strict_slashes=False)
def index_route():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    return 'C {}'.format(escape(text.replace("_", " ")))


@app.route('/python')
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    return 'Python {}'.format(escape(text.replace("_", " ")))


@app.route('/number/<n>', strict_slashes=False)
def number_route(n):
    try:
        n = int(n)
        return '{} is a number'.format(escape(n))
    except ValueError:
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
