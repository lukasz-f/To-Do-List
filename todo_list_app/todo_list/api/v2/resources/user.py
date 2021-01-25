from flask_restful import Resource
from flask import request, make_response
import requests
from datetime import datetime
from pytz import timezone
from sqlalchemy.exc import SQLAlchemyError
from http import HTTPStatus

from todo_list.api.v2.schemas.user import UserSchema
from todo_list.models.db.task import Task
from todo_list.api.v2.schemas.task import TaskSchema
from todo_list.models.db.task import db
from todo_list.models.popo.user import user_manager, User

user_schema = UserSchema()


class UserResource(Resource):
    pass


class UserListResource(Resource):
    def post(self):
        json_data = request.get_json()

        errors = user_schema.validate(json_data)

        if errors:
            response = {
                'message': 'Validation errors',
                'errors': errors
            }
            return response, HTTPStatus.BAD_REQUEST

        data = user_schema.load(json_data)

        if user_manager.get_by_username(data['username']):
            return {'message': 'username already used'}, HTTPStatus.BAD_REQUEST

        if user_manager.get_by_email(data['email']):
            return {'message': 'email already used'}, HTTPStatus.BAD_REQUEST

        user = User(**data)
        user_manager.insert_user(user)
        return user_schema.dump(user), HTTPStatus.CREATED
