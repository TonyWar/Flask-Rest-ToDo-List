from marshmallow import fields
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    is_done = db.Column(db.Boolean(), default=False)
    creation_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp())


class TodoSchema(ma.Schema):
    id = fields.Integer()
    title = fields.String(required=True)
    is_done = fields.Boolean()
