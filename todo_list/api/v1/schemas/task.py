from flask_restful import fields, reqparse

from todo_list.models.popo.task import task_manager

task_fields = {
    'id': fields.Integer,
    'uri': fields.Url('api_v1.message_endpoint'),
    'content': fields.String,
    'creation_date': fields.DateTime(dt_format='iso8601'),
    'completed': fields.Boolean
}


def task_exists(id, name):
    id = int(id)

    if id not in task_manager.tasks:
        raise ValueError("Task {0} doesn't exist".format(id))

    return id


task_creation_req_parser = reqparse.RequestParser()
task_creation_req_parser.add_argument('content', type=str, required=True, location='json', help="Content can't be blank")

task_exists_req_parser = reqparse.RequestParser()
task_exists_req_parser.add_argument('id', type=task_exists, required=True, location='view_args')

task_update_req_parser = task_exists_req_parser.copy()
task_update_req_parser.add_argument('content', type=str, location='json')
task_update_req_parser.add_argument('completed', type=bool, location='json')
