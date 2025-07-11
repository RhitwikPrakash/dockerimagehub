## FOR UNIT TESTING, WE CREATE TEST CASES HERE

from app import app
import pytest

def test_home():  # For Pytest library
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b"Hello, World! This is a Flask app running in a Docker container."