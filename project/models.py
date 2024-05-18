from flask_login import UserMixin
from sqlalchemy import TIMESTAMP
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(100), unique=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Reqs(db.Model):
    __tablename__ = 'Reqs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(1000))
    poster = db.Column(db.String(100))
    image = db.Column(db.String(100), unique=True)
    time_created = db.Column(TIMESTAMP)
    comments = db.relationship('Comment', backref=db.backref('Reqs', lazy=True))

class Comment(db.Model):
    __tablename__ = 'Comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(1000))
    req_id = db.Column(db.Integer, db.ForeignKey('Reqs.id'))
    poster = db.Column(db.String(1000))
    time_created = db.Column(TIMESTAMP)
