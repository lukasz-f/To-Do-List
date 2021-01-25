from flask_restful import Resource
from flask import request, make_response
from http import HTTPStatus
from datetime import datetime
from pytz import timezone
from sqlalchemy.exc import SQLAlchemyError

from todo_list.models.db.task import Task
from todo_list.api.v2.schemas.task import TaskSchema
from todo_list.models.db.task import db


class TaskResource(Resource):
    def get(self, id):
        task = Task.query.get_or_404(id)

        task_schema = TaskSchema()
        result = task_schema.dump(task)
        return result

    def patch(self, id):
        task = Task.query.get_or_404(id)
        task_dict = request.get_json()
        if not task_dict:
            resp = {'message': 'No input data provided'}
            return resp, HTTPStatus.BAD_REQUEST

        task_schema = TaskSchema()
        errors = task_schema.validate(task_dict)
        if errors:
            return errors, HTTPStatus.BAD_REQUEST
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
            return resp, HTTPStatus.BAD_REQUEST

    def delete(self, id):
        task = Task.query.get_or_404(id)
        try:
            delete = task.delete(task)
            response = make_response()
            return response, HTTPStatus.NO_CONTENT
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = {"error": str(e)}
            return resp, HTTPStatus.UNAUTHORIZED


class TaskListResource(Resource):
    def get(self):
        tasks = Task.query.all()

        task_schema = TaskSchema(many=True)
        result = task_schema.dump(tasks)
        return result

    def post(self):
        request_dict = request.get_json()
        if not request_dict:
            response = {'message': 'No input data provided'}
            return response, HTTPStatus.BAD_REQUEST

        task_schema = TaskSchema()
        errors = task_schema.validate(request_dict)
        if errors:
            return errors, HTTPStatus.BAD_REQUEST
        try:
            # create a new Message
            task = Task(
                content=request_dict['content'],
                creation_date=datetime.now(tz=timezone('Europe/Warsaw')))
            task.add(task)
            query = Task.query.get(task.id)
            result = task_schema.dump(query)
            return result, HTTPStatus.CREATED
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = {"error": str(e)}
            return resp, HTTPStatus.BAD_REQUEST
