#!/usr/bin/python3
"""Starts a Flask wa, server must listen 0.0.0.0 port 5000.
   route (/states_list)"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def web_page_states():
    st = storage.all(State).values()
    return render_template("7-states_list.html", states=st)

@app.route("/states/<id>", strict_slashes=False)
def web_page_id(id):
    st = storage.all(State).values()
    value = ""
    flag = False
    for i in st:
        if id in i.id:
            value = i
            flag = True
            break
        else:
            flag = False     
    return render_template("9-states.html", states=value, flag=flag)



@app.teardown_appcontext
def clear(self):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
