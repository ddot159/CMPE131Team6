from app import db
from datetime import datetime
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=False)
    email = db.Column(db.String(32), unique=True, nullable=False, index=True)
    password = db.Column(db.String(200), unique=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(256))
    date = db.Column(db.DateTime, default=datetime.utcnow)
