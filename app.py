# This is a simple Flask application that can be run in a Docker container.
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! This is a Flask app running in a Docker container."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) # Run the app on all available interfaces at port 5000

