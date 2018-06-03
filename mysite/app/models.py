from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db, login
from flask_login import UserMixin

# Create a db model for instances of users with parameters 'id', 'username',
# 'email', 'password hash' with foreign key relationships to all other tables.
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    articles = db.relationship('Article', backref='author', lazy='dynamic')
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    projects = db.relationship('Project', backref='author', lazy='dynamic')

    # When called, display the instance as '<User username>'
    def __repr__(self):
        return '<User {}>'.format(self.username)

    # Method to set a password based on a hash of said password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Method to check password hash against the stored hash of the password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Create a database model for instances of articles with 'id', 'body', 'timestamp',
# 'url', 'imageurl'*, and 'user_id' as a foreign key to the user creating the instance
# *'image url' has been changed due to adding compatibility with 'flask_upload'
# to only require the filename and filetype of the image as the url for the
# static/img folder is included within the method to assign said image url
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    url = db.Column(db.String(500))
    imageurl = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # When called, display the instance as '<Article body>'
    def __repr__(self):
        return '<Article {}>'.format(self.body)

# Create a database model for instances of blog posts with 'id', 'title', 'body',
# 'timestamp', 'imageurl'*, and 'user id' as a foreign key to the user creating
# the instance
# *'image url' has been changed due to adding compatibility with 'flask_upload'
# to only require the filename and filetype of the image as the url for the
# static/img folder is included within the method to assign said image url
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), index=True)
    body = db.Column(db.String(1000), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    imageurl = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship(User)

    # When called, display '<Post title>'
    def __repr__(self):
        return '<Post {}>'.format(self.title)

# Create a database model for instances of recent projects with 'id', 'title',
# 'body', 'timestamp', 'url', 'image url'*, and 'user id' as a foreign key for the
# user creating the instance
# *'image url' has been changed due to adding compatibility with 'flask_upload'
# to only require the filename and filetype of the image as the url for the
# static/img folder is included within the method to assign said image url
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), index=True)
    body = db.Column(db.String(10000), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    url = db.Column(db.String(500))
    imageurl = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship(User)

    # When called, display '<Post title>'
    def __repr__(self):
        return '<Post {}>'.format(self.title)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
