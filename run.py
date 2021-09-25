from app import db, create_app
from app.blueprints.main.models import MarvelCharacter
from app.blueprints.auth.models import User


app = create_app()

@app.shell_context_processor
def make_context():
    return{
        'MarvelCharacter': MarvelCharacter,
        'User' : User,
        'db' : db
    }