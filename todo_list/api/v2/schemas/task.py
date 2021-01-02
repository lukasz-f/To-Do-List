from marshmallow import Schema, fields, pre_load
from marshmallow import validate
from todo_list.app import ma


# Flask-Marshmallow features allow to automatically determine the type for each attribute
# based on the fields declared in a model
class TaskSchema(ma.Schema):
    id = fields.Integer(dump_only=True)  # read-only
    content = fields.String(required=True, validate=validate.Length(1))  # minimum length of 1 characters
    creation_date = fields.DateTime()
    completed = fields.Boolean()
    url = ma.URLFor('api_v2.taskresource', id='<id>', _external=True)
