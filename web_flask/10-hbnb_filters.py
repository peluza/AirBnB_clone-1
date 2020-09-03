#!/usr/bin/python3
"""Starts a Flask wa, server must listen 0.0.0.0 port 5000.
   route (/hbnb_filters)"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def state_city_list():
    st = storage.all(State).values()
    am = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html", states=st, ameny=am)


@app.teardown_appcontext
def clear(self):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
