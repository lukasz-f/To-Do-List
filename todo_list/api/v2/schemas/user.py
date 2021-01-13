from marshmallow import Schema, fields, pre_load
from marshmallow import validate
from todo_list.app import ma


class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)  # skip during deserialization
    username = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.Method(required=True, deserialize='load_password')

    def load_password(self, value):
        return value
