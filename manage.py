from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = '/login'
    login_manager.login_message_category = 'danger'


    # register blueprints
    from users.views import users_app
    app.register_blueprint(users_app)


    # retrun the app instance
    return app
