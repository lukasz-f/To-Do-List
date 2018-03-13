## To-Do-List

### Python + REST + Flask

### REST API:
- localhost:5000/api/v1/tasks GET; 200 OK - return all tasks
- tasks POST; 201 Created - create task
- tasks/{id} GET; 200 OK, 404 Not Found - get task with id
- tasks/{id} PATCH; 200 OK, 400 Bad Request, 404 Not Found - update task with id
- tasks/{id} DELETE; 204 No Content, 404 Not Found - delete task with id
