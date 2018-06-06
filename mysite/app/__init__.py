from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Message, Mail
import local_settings

mail = Mail()

# Assign the flask app
app = Flask(__name__)


app.config['SECRET_KEY'] = local_settings.SECRET_KEY

# Assign the directory of photo uploads
app.config['UPLOADED_PHOTOS_DEST'] = 'app/static/img'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'frankiebaffa.com@gmail.com'

# Define the password within a local file 'local_settings.py' as:
#       MAIL_PASSWORD = 'password-of-your-choice'
app.config["MAIL_PASSWORD"] = local_settings.MAIL_PASSWORD

photos = UploadSet('photos', IMAGES)

# Configure the application based on the contents of 'config.py'
app.config.from_object(Config)

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
        View('About', 'aboutme'),
        View('Contact', 'contact'))
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
        View('Contact', 'contact'),
        View('Upload', 'upload'),
        View('Logout', 'logout'))
    nav.register_element('top', navconfig)
    return navconfig

# Initialize an instance of 'flask_nav' within the flask application
nav.init_app(app)

# Initialize an instance of 'flask_nav' within the flask application
mail.init_app(app)

# Only execute when module is run as a program
if __name__ == '__main__':
    app.run()
