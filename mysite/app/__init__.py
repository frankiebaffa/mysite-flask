from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)
photos = UploadSet('photos', IMAGES)
app.config.from_object(Config)
app.config['UPLOADED_PHOTOS_DEST'] = 'app/static/img'
configure_uploads(app, photos)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from app import routes

Bootstrap(app)

nav = Nav()
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

nav.init_app(app)


if __name__ == '__main__':
    app.run()
