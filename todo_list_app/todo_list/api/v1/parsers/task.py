from flask_restful import reqparse


task_creation_req_parser = reqparse.RequestParser()
task_creation_req_parser.add_argument('content', type=str, required=True, location='json', help="Content can't be blank")

task_read_req_parser = reqparse.RequestParser()
task_read_req_parser.add_argument('id', type=int, required=True, location='view_args')

task_update_req_parser = task_read_req_parser.copy()
task_update_req_parser.add_argument('content', type=str, location='json')
task_update_req_parser.add_argument('completed', type=bool, location='json')
