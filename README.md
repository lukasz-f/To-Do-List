## To-Do-List

### Python + REST + Flask + Marshmallow + SQLAlchemy + SQLite + unittest

### REST API:
- localhost:5000/todo/api/v1.0/tasks GET; 200 OK - return all tasks
- tasks POST; 201 Created - create task
- tasks/{id} GET; 200 OK, 404 Not Found - get task with id
- tasks/{id} PATCH; 200 OK, 400 Bad Request, 404 Not Found - update task with id
- tasks/{id} DELETE; 204 No Content, 404 Not Found - delete task with id

### Prerequisites
- Python 3.6
- virtualenv
- pip
- requests
- flask-restful
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Script
- marshmallow
- marshmallow-sqlalchemy
- Flask-Marshmallow
