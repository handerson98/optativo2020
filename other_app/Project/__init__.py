from flask import Flask


def create_app():
    app = Flask(__name__)
    registerBlueprints(app)
    return app



def registerBlueprints(app):
    from Project.rename.endpoints_rename import renameBlueprints
    app.register_blueprint(renameBlueprints)
