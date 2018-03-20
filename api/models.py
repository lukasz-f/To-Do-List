class TaskModel:
    def __init__(self, content, creation_date):
        self.id = 0  # We will automatically generate the new id
        self.content = content
        self.creation_date = creation_date
        self.completed = False
