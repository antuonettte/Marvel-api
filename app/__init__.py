from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_manager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app)

    with app.app_context():
        from app.blueprints.main import bp as main
        app.register_blueprint(main)

        from app.blueprints.auth import bp as auth
        app.register_blueprint(auth)

    return app