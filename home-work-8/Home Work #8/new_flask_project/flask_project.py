from flask import Flask
from config import FlaskConfig
from database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(FlaskConfig)
    db.init_app(app)

    import authentification

    app.register_blueprint(authentification.auth)
    return app


app = create_app()
