from todo_list.app import db


class AddUpdateDelete():
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()


class Task(db.Model, AddUpdateDelete):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(250), unique=True, nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, server_default='false')

    def __init__(self, content, creation_date):
        self.id = 0  # We will automatically generate the new id
        self.content = content
        self.creation_date = creation_date
        self.completed = False
