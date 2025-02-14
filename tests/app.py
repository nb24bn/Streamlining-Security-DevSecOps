"""
This module contains the main application logic for the Flask app.
"""
from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    """
    Endpoint for the home page.
    Returns a welcome message.
    """
    return "Welcome to DevSecOps!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
