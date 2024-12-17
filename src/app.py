"""
This module contains the main application logic for the DevSecOps project.
"""
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    """
    Home route of the application.

    Returns:
        str: A welcome message.
    """
    return "Welcome to the DevSecOps App!"

if __name__ == "__main__":
     app.run(
        host=os.getenv("FLASK_RUN_HOST", "127.0.0.1"),
        port=int(os.getenv("FLASK_RUN_PORT", 5000))
    )

