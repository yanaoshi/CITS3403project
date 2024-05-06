from flask_login import UserMixin
from sqlalchemy import TIMESTAMP
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100), unique = True)

class Reqs(db.Model):
    __tablename__ = 'Reqs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(1000))
    poster = db.Column(db.String(100))
    image = db.Column(db.String(100), unique = True)
    time_created = db.Column(TIMESTAMP)
    comments = db.relationship('Comment', backref=db.backref('Reqs', lazy=True))

class Comment(db.Model):
    __tablename = 'Comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(1000))
    req_id = db.Column(db.Integer, db.ForeignKey('Reqs.id'))
    poster = db.Column(db.String(1000))
    time_created = db.Column(TIMESTAMP)
