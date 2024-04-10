#!/usr/bin/python3
"""Starts a Flask web application
"""
from models import storage
from flask import Flask, render_template
from models.city import City
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Get cities by states"""
    list_states = storage.all(State)
    list_cities = storage.all(City)
    return render_template('8-cities_by_states.html', cities=list_cities,
                           states=list_states)


@app.teardown_appcontext
def remove_current_session(exception):
    """Close the SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
