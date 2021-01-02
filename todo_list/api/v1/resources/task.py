from flask_restful import Resource, marshal_with
import requests
from datetime import datetime
from pytz import timezone

from todo_list.api.v1.schemas.task import task_fields, task_creation_req_parser, task_update_req_parser, task_exists_req_parser
from todo_list.models.popo.task import task_manager, Task


class IndexResource(Resource):
    def get(self):
        return 'To-Do List REST app'


class TaskListResource(Resource):
    @marshal_with(task_fields)
    def get(self):
        return task_manager.get_all_tasks()

    @marshal_with(task_fields)
    def post(self):
        args = task_creation_req_parser.parse_args()
        task = Task(
            content=args['content'],
            creation_date=datetime.now(tz=timezone('Europe/Warsaw'))
        )
        task_manager.insert_task(task)
        return task, requests.codes.created


class TaskResource(Resource):
    @marshal_with(task_fields)
    def get(self, id):
        task_exists_req_parser.parse_args()
        return task_manager.get_task(id)

    @marshal_with(task_fields)
    def patch(self, id):
        args = task_update_req_parser.parse_args()
        task = task_manager.get_task(id)
        if 'content' in args and args['content'] is not None:
            task.content = args['content']
        if 'completed' in args and args['completed'] is not None:
            task.completed = args['completed']
        return task

    def delete(self, id):
        task_exists_req_parser.parse_args()
        return task_manager.delete_task(id), requests.codes.no_content
