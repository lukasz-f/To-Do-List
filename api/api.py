from flask import Flask
from flask_restful import Api, Resource, marshal_with, fields, abort, reqparse
import requests
from datetime import datetime
from pytz import timezone
from models import TaskModel


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
task_manager.insert_task(TaskModel('task', datetime.now()))
task_manager.insert_task(TaskModel('task', datetime.utcnow()))

task_fields = {
    'id': fields.Integer,
    'uri': fields.Url('message_endpoint'),
    'content': fields.String,
    'creation_date': fields.DateTime(dt_format='iso8601'),
    'completed': fields.Boolean
}


class Index(Resource):
    def get(self):
        return 'To-Do List REST app'


class TaskList(Resource):
    @marshal_with(task_fields)
    def get(self):
        return task_manager.get_all_tasks()

    @marshal_with(task_fields)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('content', type=str, required=True, help="Content can't be blank")
        args = parser.parse_args()
        task = TaskModel(
            content=args['content'],
            creation_date=datetime.now(tz=timezone('Europe/Warsaw'))
        )
        task_manager.insert_task(task)
        return task, requests.codes.created


class Task(Resource):
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


app = Flask(__name__)
api = Api(app)
api.add_resource(Index, '/todo/api')
api.add_resource(TaskList, '/todo/api/v1.0/tasks')
api.add_resource(Task, '/todo/api/v1.0/task/<int:id>', endpoint='message_endpoint')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
