from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from models import db
    db.init_app(app)
    db.app = app
    db.create_all()  # create the tables and database

    from views import api_bp
    app.register_blueprint(api_bp, url_prefix='/todo/api/v2.0')

    return app
