"""
Tests: test_app
Description: Contains unit tests for the app module.
"""

#def test_app_home():
 #   """Tests the home route of the application."""
 #   response = "Welcome to the DevSecOps App!"
  #  assert "DevSecOps" in response
from src.app import home  # Import the actual function being tested

def test_app_home():
    """Tests the home route of the application."""
    response = home()  # Call the function from the app
    assert "DevSecOps" in response  # Assert that "DevSecOps" is in the response
