#!/usr/bin/python3
"""Starts a Flask wa, server must listen 0.0.0.0 port 5000.
   route (/states_list)"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def web_page():
    st = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=st)


@app.teardown_appcontext
def clear(self):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
