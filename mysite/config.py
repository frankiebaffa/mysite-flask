import os

# Assign the base directory based on where the main flask app resides
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Create a secret key for CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Seed in dirt'

    # Assign the location of the sqlite3 database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
