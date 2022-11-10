#!/usr/bin/python3
"""
   Starts a flask web app
"""
from flask import Flask

app = Flask('__main__')


@app.route('/', strict_slashes=False)
def index_route():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
