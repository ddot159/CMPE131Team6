# same as
# from app import db
from app import db
from datetime import datetime
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=False)
    password = db.Column(db.String(200), unique=False)
    lists = db.relationship('List', backref='user', lazy='dynamic')
    posts = db.relationship('Task', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.id)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Posts {}>'.format(self.body)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(256), unique=False, nullable=False)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    task_name = db.Column(db.String, db.ForeignKey('list.name'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return '<Task {}>'.format(self.item)


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=False, nullable=False)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    category = db.Column(db.String(256), unique=False, nullable=False)
    priority = db.Column(db.Boolean, unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tasks = db.relationship('Task', backref = 'task', lazy = 'dynamic')
    created = db.Column(db.DateTime)
    due = db.Column(db.DateTime)
    def __repr__(self):
        return '{}'.format(self.id)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
