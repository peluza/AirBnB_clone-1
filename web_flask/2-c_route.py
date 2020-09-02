#!/usr/bin/python3
"""starts a Flask web application:
        must be listening on 0.0.0.0, port 5000
    """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """index

    Returns:
        str: 'Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb

    Returns:
        str: HBNB
    """
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def varpage(text):
    """vatpage

    Args:
        text (str): name for the page

    Returns:
        str: name for the page
    """
    var = str(text).replace("_", " ")
    return "C " + var


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
