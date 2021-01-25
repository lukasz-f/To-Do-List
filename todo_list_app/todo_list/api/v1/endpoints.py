from flask import Blueprint
from flask_restful import Api

from todo_list.api.v1.resources.task import IndexResource, TaskListResource, TaskResource


api_v1_bp = Blueprint('api_v1', __name__)
api = Api(api_v1_bp)
api.add_resource(IndexResource, '/')
api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/task/<int:id>', endpoint='message_endpoint')
