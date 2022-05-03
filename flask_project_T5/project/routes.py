from flask import Flask, render_template, flash

from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from project import myapp_obj

#myapp_obj = Flask(__name__)

@login_required
@myapp_obj.route('/')
def index():
    return render_template('index.html')

@myapp_obj.route('/profile')
def profile():
    return render_template('profile.html')

@myapp_obj.route('/logout')
def logout():
    return 'Logout'

@myapp_obj.route('/login')
def login():
    return render_template('login.html')

@myapp_obj.route('/signup')
def signup():
    return render_template('signup.html')