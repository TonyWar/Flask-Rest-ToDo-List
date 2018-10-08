from flask import request
from flask_restful import Resource
from app.models.todo import db, Todo, TodoSchema

todos_schema = TodoSchema(many=True)
todo_schema = TodoSchema()

class TodoResource(Resource):
    def get(self, todo_id):
        todo = Todo.query.filter_by(id=todo_id).first()
        if not todo:
            return {'message': 'Todo does not exist'}, 400
        
        result = todo_schema.dump(todo).data
        return {'status': 'success', 'data': result}, 202

    def put(self, todo_id):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        
        todo = Todo.query.filter_by(id=todo_id).first()
        if not todo:
            return {'message': 'Todo does not exist'}, 400

        if 'title' in json_data:
            todo.title = json_data['title']
        if 'is_done' in json_data:
            todo.is_done = json_data['is_done']
        db.session.commit()

        result = todo_schema.dump(todo).data

        return {'status': 'success', 'data': result}, 204

    def delete(self, todo_id):
        todo = Todo.query.filter_by(id=todo_id)
        if not todo:
            return {'message': 'Todo does not exist'}, 400
        todo = todo.delete()
        db.session.commit()

        result = todo_schema.dump(todo).data

        return {'status': 'success', 'data': result}, 204
