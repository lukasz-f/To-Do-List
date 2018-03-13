from flask import Flask
from flask_restful import Api, Resource, marshal_with, fields, abort, reqparse
import requests
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
        del self.tasks[id]


task_manager = TaskManager()
task_manager.insert_task(TaskModel('task'))

task_fields = {
    'id': fields.Integer,
    'content': fields.String
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
        parser.add_argument('id', type=int)
        parser.add_argument('content', type=str)
        args = parser.parse_args()
        task = TaskModel(
            content=args['content']
        )
        task_manager.insert_task(task)
        return task, requests.codes.created


class Task(Resource):
    def abort_if_task_doesnt_exist(self, id):
        if id not in task_manager.tasks:
            abort(requests.codes.not_found, message="Message {0} doesn't exist".format(id))

    @marshal_with(task_fields)
    def get(self, id):
        self.abort_if_task_doesnt_exist(id)
        return task_manager.get_task(id)

#     @marshal_with(task_fields)
#     def patch(self, id):
#         pass
#
    def delete(self, id):
        self.abort_if_task_doesnt_exist(id)
        return task_manager.delete_task(id), requests.codes.no_content


app = Flask(__name__)
api = Api(app)
api.add_resource(Index, '/api')
api.add_resource(TaskList, '/api/v1/tasks')
# api.add_resource(Task, '/api/v1/task/<int:id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
