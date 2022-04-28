from app import myapp_obj
from flask import render_template, flash

from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required


@login_required
@myapp_obj.route('/')
def home():
    return 'home'

@myapp_obj.route('/login')
def login():
    # create a form
    # validate form input
    # if input is valid
    #     check username & password matches the one in db
    #     if true
    # user = User.query.filter_by(....)
    login_user(user)

