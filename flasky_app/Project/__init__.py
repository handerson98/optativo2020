from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import marshmallow, sqlalchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
migrate = Migrate()
marsh = Marshmallow()


def createApp():

    app = Flask(__name__)
    app.config.from_object(DBConfig)

    db.init_app(app)
    marsh.init_app(app)
    migrate.init_app(app,db)

    blueprintConfig(app)
    error_handler(app)

    return app

def blueprintConfig(app):
    from Project.User.endPointUser import userBlueprint
    app.register_blueprint(userBlueprint)


def error_handler(app):

    @app.errorhandler(marshmallow.exceptions.ValidationError)
    def validationErrorHandler(event):
        return event.messages, 400

    @app.errorhandler(sqlalchemy.exc.ProgrammingError)
    def ProgrammingError(event):
        return "problema con las migraciones !!!", 500

class DBConfig:
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@postgres-db:5432/flask_example'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
