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
    """Get the list of all states and cities by states"""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    for state in states:
        state.cities = sorted(state.cities, key=lambda y: y.name)
        state.state_ref = state.id
        for city in state.cities:
            city.city_ref = city.id
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def remove_current_session(exception):
    """Close the SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
