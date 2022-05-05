from flask import Flask, render_template, flash

from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from app import myapp_obj

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
    # create a form
    # validate form input
    # if input is valid
    #     check username & password matches the one in db
    #     if true
    #email = request.form.get("email")
    #password = request.form.get("password")
    #user = User.query.filter_by(email=email).first()

    #login_user(user)

@myapp_obj.route('/signup')
def signup():
    return render_template('signup.html')
