from flask import Blueprint
from flask_restful import Api

from todo_list.api.v2.resources.task import TaskListResource, TaskResource
from todo_list.api.v2.resources.user import UserListResource, UserResource

api_v2_bp = Blueprint('api_v2', __name__)
api = Api(api_v2_bp)

api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/tasks/<int:id>')

api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:id>')
