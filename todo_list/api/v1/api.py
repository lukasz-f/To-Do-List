from flask import Blueprint
from flask_restful import Api, Resource, marshal_with, fields, abort, reqparse
import requests
from datetime import datetime
from pytz import timezone


class Task:
    def __init__(self, content, creation_date):
        self.id = 0  # We will automatically generate the new id
        self.content = content
        self.creation_date = creation_date
        self.completed = False


class TaskManager:
    last_id = 0

    def __init__(self):
        self.tasks = {}

    def get_all_tasks(self):
        return [v for v in self.tasks.values()]

    def get_task(self, id):
        return self.tasks[id]

    def insert_task(self, task):
        self.__class__ .last_id += 1
        task.id = self.__class__.last_id
        self.tasks[task.id] = task

    def update_task(self, task):
        self.tasks[task.id] = task.copy()

    def delete_task(self, id):
        del(self.tasks[id])


task_manager = TaskManager()
task_manager.insert_task(Task('task 1', datetime.now()))
task_manager.insert_task(Task('task 2', datetime.utcnow()))

task_fields = {
    'id': fields.Integer,
    'uri': fields.Url('api_v1.message_endpoint'),
    'content': fields.String,
    'creation_date': fields.DateTime(dt_format='iso8601'),
    'completed': fields.Boolean
}


class IndexResource(Resource):
    def get(self):
        return 'To-Do List REST app'


class TaskListResource(Resource):
    @marshal_with(task_fields)
    def get(self):
        return task_manager.get_all_tasks()

    @marshal_with(task_fields)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('content', type=str, required=True, help="Content can't be blank")
        args = parser.parse_args()
        task = Task(
            content=args['content'],
            creation_date=datetime.now(tz=timezone('Europe/Warsaw'))
        )
        task_manager.insert_task(task)
        return task, requests.codes.created


class TaskResource(Resource):
    def abort_if_task_doesnt_exist(self, id):
        if id not in task_manager.tasks:
            abort(requests.codes.not_found, content="Task {0} doesn't exist".format(id))

    @marshal_with(task_fields)
    def get(self, id):
        self.abort_if_task_doesnt_exist(id)
        return task_manager.get_task(id)

    @marshal_with(task_fields)
    def patch(self, id):
        self.abort_if_task_doesnt_exist(id)
        task = task_manager.get_task(id)
        parser = reqparse.RequestParser()
        parser.add_argument('content', type=str)
        parser.add_argument('completed', type=bool)
        args = parser.parse_args()
        if 'content' in args and args['content'] is not None:
            task.content = args['content']
        if 'completed' in args and args['completed'] is not None:
            task.completed = args['completed']
        return task

    def delete(self, id):
        self.abort_if_task_doesnt_exist(id)
        return task_manager.delete_task(id), requests.codes.no_content


api_v1_bp = Blueprint('api_v1', __name__)
api = Api(api_v1_bp)
api.add_resource(IndexResource, '/')
api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/task/<int:id>', endpoint='message_endpoint')
