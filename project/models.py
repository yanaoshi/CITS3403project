from flask_login import UserMixin
from sqlalchemy import func, TIMESTAMP, text
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100), unique = True)

class Reqs(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(1000))
    poster = db.Column(db.String(100))
    image = db.Column(db.String(100), unique = True)
    time_created = db.Column(TIMESTAMP)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(1000))
    req_id = db.Column(db.Integer, db.ForeignKey('reqs.id'))
    commenter_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    time_created = db.Column(TIMESTAMP)
