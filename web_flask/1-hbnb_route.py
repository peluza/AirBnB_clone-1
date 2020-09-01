#!/usr/bin/python3
"""starts a Flask web application:
        must be listening on 0.0.0.0, port 5000
    """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


app.run(host='0.0.0.0', port=5000)
