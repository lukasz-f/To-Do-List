from marshmallow import fields
from marshmallow import validate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()  # create the SQLAlchemy instance before the Marshmallow instance
ma = Marshmallow()


class AddUpdateDelete:
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()


class Task(db.Model, AddUpdateDelete):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(250), unique=True, nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, server_default='false')

    def __init__(self, content, creation_date):
        self.id = 0  # We will automatically generate the new id
        self.content = content
        self.creation_date = creation_date
        self.completed = False


# Flask-Marshmallow features allow to automatically determine the type for each attribute
# based on the fields declared in a model
class TaskSchema(ma.Schema):
    id = fields.Integer(dump_only=True)  # read-only
    content = fields.String(required=True, validate=validate.Length(1))  # minimum length of 1 characters
    creation_date = fields.DateTime()
    completed = fields.Boolean()
    url = ma.URLFor('api.taskresource', id='<id>', _external=True)
