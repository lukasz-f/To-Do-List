from flask_restful import fields

task_fields = {
    'id': fields.Integer,
    'uri': fields.Url('api_v1.message_endpoint'),
    'content': fields.String,
    'creation_date': fields.DateTime(dt_format='iso8601'),
    'completed': fields.Boolean
}
