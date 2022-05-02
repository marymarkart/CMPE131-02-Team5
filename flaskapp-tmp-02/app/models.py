from app import db
from datetime import datetime
from app import login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    #email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))
    authenticated = db.Column(db.Boolean, default=False)
    posts = db.relationship('Post')#, backref='author', lazy='dynamic')

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User: {self.username}>'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body= db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<User ID: {self.user_id} {self.body}>'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))