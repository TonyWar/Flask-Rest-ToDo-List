from flask import Blueprint
from flask_restful import Api
from app.todos.routes import TodosResource

bp = Blueprint('todos', __name__)
api = Api(bp)

api.add_resource(TodosResource, '/')
