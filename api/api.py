from flask import Flask
from flask_restful import Api, Resource, marshal_with, fields
from models import TaskModel
import status


class TaskManager:
    last_id = 0

    def __init__(self):
        self.tasks = {}

    def insert_message(self, task):
        self.__class__ .last_id += 1
        task.id = self.__class__.last_id
        self.tasks[task.id] = task

    def get_message(self, id):
        return self.tasks[id]

    def delete_message(self, id):
        del self.tasks[id]


task_manager = TaskManager()
task_manager.insert_message(TaskModel('task'))

task_fields = {
    'id': fields.Integer,
    'content': fields.String
}


class TaskList(Resource):
    @marshal_with(task_fields)
    def get(self):
        return [v for v in task_manager.tasks.values()]


class Index(Resource):
    def get(self):
        return 'Flask app'


app = Flask(__name__)
api = Api(app)
api.add_resource(Index, '/api')
api.add_resource(TaskList, '/api/tasks')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
