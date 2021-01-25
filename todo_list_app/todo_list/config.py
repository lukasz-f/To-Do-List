import os

# You need to replace the next values with the appropriate values for your configuration
basedir = os.path.abspath(os.path.dirname(__file__))
ENV = os.getenv("FLASK_ENV")
DEBUG = ENV == "development"
PORT = 5000
HOST = "0.0.0.0"
SECRET_KEY = os.getenv("SECRET_KEY")
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
