# Import necessary modules and classes
from flask import Flask
from config import Config


# Create a Flask application instance
app = Flask(__name__)

# Set the secret key for the application (Change this to a secure, random key)
app.secret_key = 'your_secret_key'

# Set the session to non-permanent (session will expire when the browser is closed)
app.permanent_session_lifetime = False

# Import routes from the 'app' module (You should have an 'app.py' file in your project)
from app import routes
