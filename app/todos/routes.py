from app.todos import bp

@bp.route('/')
def hello_world():
  return 'Hello world'