# Import the 'app' instance from the 'app' module
from app import app

# Check if this script is the main entry point of the application
if __name__ == '__main__':
    # Start the Flask application with debugging enabled, allowing external accessfro
    # Debug mode should be turned off in production for security reasons
    app.run(debug=True, host='0.0.0.0', port=8000)
