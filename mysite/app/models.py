from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db, login
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    articles = db.relationship('Article', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    url = db.Column(db.String(500))
    imageurl = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Article {}>'.format(self.body)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), index=True)
    body = db.Column(db.String(10000), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    imageurl = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Article {}>'.format(self.title)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), index=True)
    body = db.Column(db.String(10000), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    url = db.Column(db.String(500))
    imageurl = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Article {}>'.format(self.title)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
