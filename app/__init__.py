from flask import Flask, request, current_app
from config import Config

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)

  # blueprints
  from app.todos import bp as todos_bp
  app.register_blueprint(todos_bp, url_prefix='/todo')

  return app

# from app import models