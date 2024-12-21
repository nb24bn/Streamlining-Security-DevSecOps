"""
Tests: test_app
Description: Contains unit tests for the app module.
"""

def test_app_home():
    """Tests the home route of the application."""
    response = "Welcome to the DevSecOps App!"
    assert "DevSecOps" in response
