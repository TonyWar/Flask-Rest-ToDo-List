from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # blueprints
    from app.todos import bp as todos_bp
    app.register_blueprint(todos_bp, url_prefix='/todo')

    from app.models.todo import db as todo_db
    todo_db.init_app(app)

    return app

# from app import models
