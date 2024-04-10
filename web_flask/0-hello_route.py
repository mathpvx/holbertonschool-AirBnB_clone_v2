#!/usr/bin/python3
"""Starts a Flask web application."""


from flask import Flask

# Create a Flask application instance
app = Flask(__name__)


# Define route for the root URL with more flexibility with trailing slashes
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


# run the app if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
