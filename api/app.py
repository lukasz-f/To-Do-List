from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from api import api_v1_bp
    app.register_blueprint(api_v1_bp, url_prefix='/api/v1')

    from models import db
    db.init_app(app)
    db.app = app
    db.create_all()  # create the tables and database

    from views import api_v2_bp
    app.register_blueprint(api_v2_bp, url_prefix='/api/v2')

    return app
