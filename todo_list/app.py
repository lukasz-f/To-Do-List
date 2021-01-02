from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()  # create the SQLAlchemy instance before the Marshmallow instance
ma = Marshmallow()


def create_app():
    app = Flask(__name__)
    app.config.from_object('todo_list.config')

    db.init_app(app)
    db.app = app
    db.create_all()  # create the tables and database

    ma.init_app(app)

    from todo_list.api.v1.views import api_v1_bp
    app.register_blueprint(api_v1_bp, url_prefix='/api/v1')

    from todo_list.api.v2.views import api_v2_bp
    app.register_blueprint(api_v2_bp, url_prefix='/api/v2')

    return app
