from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from todo_list.models.db.task import db
from todo_list.run import app

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
