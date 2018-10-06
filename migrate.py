from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.models.todo import db as todo_db
from app import create_app

app = create_app()

migrate = Migrate(app, todo_db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()