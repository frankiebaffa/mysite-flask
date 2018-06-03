from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES

# Assign the flask app
app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

# Configure the application based on the contents of 'config.py'
app.config.from_object(Config)

# Assign the directory of photo uploads
app.config['UPLOADED_PHOTOS_DEST'] = 'app/static/img'
configure_uploads(app, photos)

# Pass the flask application into the SQLAlchemy instance when 'db' is called
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Pass the flask application into the 'flask_login' instance when 'login'
# is called
login = LoginManager(app)

# Import the routes and views defined in 'routes.py'
from app import routes

# Pass the flask application into the flask_bootstrap instance
Bootstrap(app)

# Create an instance of flask_nav called 'nav'
nav = Nav()

# Create a method definining the standard user navbar
@nav.navigation()
def mynavbar():
    navconfig = Navbar(
        'Frankie Baffa',
        View('Home', 'index'),
        View('Blog', 'blog'),
        View('Articles', 'articles'),
        View('About', 'aboutme'))
    nav.register_element('top', navconfig)
    return navconfig

# Create a method defining the admin or logged-in user navbar
@nav.navigation()
def adminnavbar():
    navconfig = Navbar(
        'Frankie Baffa',
        View('Home', 'index'),
        View('Blog', 'blog'),
        View('Articles', 'articles'),
        View('About', 'aboutme'),
        View('Manage', 'manage'),
        View('Upload', 'upload'),
        View('Logout', 'logout'))
    nav.register_element('top', navconfig)
    return navconfig

# Initialize an instance of 'flask_nav' within the flask application
nav.init_app(app)

# Only execute when module is run as a program
if __name__ == '__main__':
    app.run()
