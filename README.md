# To-Do List

## Description

### Python + REST + API Versioning + Flask + Flask-RESTful + Marshmallow + SQLAlchemy + SQLite + unittest

### REST API:
- GET /api/v1/tasks - 200 OK - return all tasks
- POST /api/v1/tasks - 201 Created - create task
- GET /api/v1/task/{id} - 200 OK - 404 Not Found - get task with id
- PATCH /api/v1/task/{id} - 200 OK - 400 Bad Request - 404 Not Found - update task with id
- DELETE /api/v1/task/{id} - 204 No Content - 404 Not Found - delete task with id

### Prerequisites
- Python 3.8
- pyenv + virtualenv
- pip ins

### App versions
- v1: simple in-memory dictionary implementation
- v2: SQLite implementation

## Run project
### Flask CLI
```
cd To-Do-List
pyenv virtualenv 3.8.3 todo-list
pyenv local todo-list
pip install -r requirements.txt
flask run
```
### Docker-compose
```
todo
```
