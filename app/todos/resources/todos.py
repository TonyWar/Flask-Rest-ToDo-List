from flask import request
from flask_restful import Resource
from app.models.todo import db, Todo, TodoSchema

todos_schema = TodoSchema(many=True)
todo_schema = TodoSchema()


class TodosResource(Resource):
    def get(self):
        todos = Todo.query.all()
        todos = todos_schema.dump(todos).data
        return {'status': 'success', 'data': todos}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, erros = todo_schema.load(json_data)
        if erros:
            return erros, 422

        todo = Todo.query.filter_by(title=data['title']).first()
        if todo:
            return {'message': 'Todo already exists'}, 400

        todo = Todo(
            title=json_data['title']
        )
        db.session.add(todo)
        db.session.commit()

        result = todo_schema.dump(todo).data

        return {'status': 'success', 'data': result}, 201
