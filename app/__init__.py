import logging
from flask import Flask
from config import Config
from flask_cors import CORS


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)

    # blueprints
    from app.todos import bp as todos_bp
    app.register_blueprint(todos_bp, url_prefix='/todo')

    from app.models.todo import db as todo_db
    todo_db.init_app(app)

    if not app.debug and not app.testing:
        if app.config['LOG_TO_STDOUT']:
              stream_handler = logging.StreamHandler()
              stream_handler.setLevel(logging.INFO)
              app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/todoList.log',
                                              maxBytes=10240, backupCount=10)
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s '
                '[in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('ToDo list startup')

    return app

# from app import models
