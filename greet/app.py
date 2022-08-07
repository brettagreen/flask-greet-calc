from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """Return simple "Welcome" Greeting."""

    return 'Welcome'

@app.route('/welcome/home')
def home():
    """Return 'welcome home'"""

    return 'Welcome Home'

@app.route('/welcome/back')
def back():
    """Return 'welcome back'"""

    return 'Welcome Back'