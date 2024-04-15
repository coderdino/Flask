from flask import Flask
from flask_sqlalchemy import SQLAlchemy # This is for database
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'iamagenius'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # If user isn't logged in
    login_manager.init_app(app)
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, urls_prefix='/')
    app.register_blueprint(auth, urls_prefix='/')  #We initialize and register these things so they can actually run in the main file.

    from .models import User, Note

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) #How we load a user.

    create_database(app)

    return app

def create_database(app):
    if not path.exists('instance/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')