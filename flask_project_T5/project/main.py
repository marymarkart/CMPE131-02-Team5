from flask import Blueprint
from . import db

main = Blueprint('main', __name__)

from flask import Blueprint, render_template
...
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')

from flask import Blueprint
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/logout')
def logout():
    return 'Logout'

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')