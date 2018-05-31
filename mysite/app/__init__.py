from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
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
        View('Articles', 'articles'),
        View('About', 'aboutme'))
    nav.register_element('top', navconfig)
    return navconfig

nav.init_app(app)


if __name__ == '__main__':
    app.run()
