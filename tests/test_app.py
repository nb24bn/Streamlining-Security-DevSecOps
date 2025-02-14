import pytest
from src.app import app  # Import your Flask app

@pytest.fixture(scope="module")
def test_client():
    """Set up the test client with app context"""
    with app.app_context():  # Push app context
        yield app.test_client()

def test_app_home(test_client):
    """Tests the home route of the application."""
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"DevSecOps" in response.data
