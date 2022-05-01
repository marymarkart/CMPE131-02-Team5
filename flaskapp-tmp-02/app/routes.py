from app import myapp_obj
from flask import Flask, render_template, flash

from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required


@login_required
@myapp_obj.route('/')
def home():
    return render_template('splash.html')


'''@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve

    """
    return User.query.get(user_id)'''


@myapp_obj.route('/login')
def login():
    # create a form
    # validate form input
    # if input is valid
    #     check username & password matches the one in db
    #     if true
    # user = User.query.filter_by(....)
    #login_user(user)
    return render_template('login.html')

@myapp_obj.route('/signup')
def signup():
    # username = request.form['username']
    # password = request.form['password']
    return render_template('signup.html')