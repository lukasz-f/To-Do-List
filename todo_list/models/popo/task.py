from datetime import datetime
from dataclasses import dataclass


@dataclass
class Task:
    content: str
    creation_date: datetime
    id: int = 0  # We will automatically generate the new id
    completed: bool = False


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
        del(self.tasks[id])


task_manager = TaskManager()
task_manager.insert_task(Task('task 1', datetime.now()))
task_manager.insert_task(Task('task 2', datetime.utcnow()))
