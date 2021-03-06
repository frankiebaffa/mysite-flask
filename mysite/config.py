import os

# Assign the base directory based on where the main flask app resides
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):# Assign the location of the sqlite3 database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
