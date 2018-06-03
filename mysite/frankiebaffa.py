from app import app, db
from app.models import User, Article

# create a flask shell context:
#   when the command 'flask shell' is run, this will allow these modules
#   to be imported automatically.
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Article': Article, 'Post': Post,
        'Project': Project}
