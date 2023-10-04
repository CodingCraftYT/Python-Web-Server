# Import necessary modules and classes
from flask import request, render_template, redirect, url_for, session, jsonify
from app import app

# Dummy user data (for testing purposes)
USERS = {
    'codingcraft': '123'
}

# Define a route for the home page ('/' URL)
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        # Display a welcome message with a link to your YouTube channel
        welcome_message = f'Welcome to, Coding Craft Web Server!   Check out my YouTube channel: <a href="https://www.youtube.com/@codingcraft" target="_blank">CodingCraft on YouTube</a>'
        return welcome_message

    if request.method == 'POST':
        # Retrieve the username and password from the form submission
        username = request.form['username']
        password = request.form['password']
        
        # Check if the user exists and the password is correct
        if username in USERS and USERS[username] == password:
            # Store the username in the session to log in the user
            session['username'] = username
            return redirect(url_for('index'))  # Redirect to the home page
    
    # Render the login form if no user is logged in or if there was a login error
    return render_template('login.html')

# Define a route for logging out ('/logout' URL)
@app.route('/logout', methods=['POST'])
def logout():
    if request.method == 'POST':
        data = request.get_json()
        if data.get('logout'):
            # Clear the session to log out the user
            session.pop('username', None)
            return jsonify({'message': 'Logged out successfully'}), 200
    return jsonify({'message': 'Invalid request'}), 400
