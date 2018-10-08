from flask import Blueprint
from flask_restful import Api
from app.todos.resources.todos import TodosResource
from app.todos.resources.todo import TodoResource

bp = Blueprint('todos', __name__)
api = Api(bp)

api.add_resource(TodosResource, '/')
api.add_resource(TodoResource, '/<int:todo_id>')
