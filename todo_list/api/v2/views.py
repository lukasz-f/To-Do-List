from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
from todo_list.models.db.task import db, Task, TaskSchema
from sqlalchemy.exc import SQLAlchemyError
import requests
from datetime import datetime
from pytz import timezone

api_v2_bp = Blueprint('api_v2', __name__)
task_schema = TaskSchema()
api = Api(api_v2_bp)


class TaskResource(Resource):
    def get(self, id):
        task = Task.query.get_or_404(id)
        result = task_schema.dump(task).data
        return result

    def patch(self, id):
        task = Task.query.get_or_404(id)
        task_dict = request.get_json()
        if not task_dict:
            resp = {'message': 'No input data provided'}
            return resp, requests.codes.bad_request
        errors = task_schema.validate(task_dict)
        if errors:
            return errors, requests.codes.bad_request
        try:
            if 'content' in task_dict:
                task.content = task_dict['content']
            if 'completed' in task_dict:
                task.completed = task_dict['completed']
            task.update()
            return self.get(id)
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = {"error": str(e)}
            return resp, requests.codes.bad_request

    def delete(self, id):
        task = Task.query.get_or_404(id)
        try:
            delete = task.delete(task)
            response = make_response()
            return response, requests.codes.no_content
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = {"error": str(e)}
            return resp, requests.codes.unauthorized


class TaskListResource(Resource):
    def get(self):
        tasks = Task.query.all()
        result = task_schema.dump(tasks, many=True)
        return result

    def post(self):
        request_dict = request.get_json()
        if not request_dict:
            response = {'message': 'No input data provided'}
            return response, requests.codes.bad_request
        errors = task_schema.validate(request_dict)
        if errors:
            return errors, requests.codes.bad_request
        try:
            # create a new Message
            task = Task(
                content=request_dict['content'],
                creation_date=datetime.now(tz=timezone('Europe/Warsaw')))
            task.add(task)
            query = Task.query.get(task.id)
            result = task_schema.dump(query)
            return result, requests.codes.created
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = {"error": str(e)}
            return resp, requests.codes.bad_request


api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/task/<int:id>')
