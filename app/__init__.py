from flask import Flask
from config import Config
from app.modelos import usuario  # noqa: F401

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

3
    db.init_app(app)


    return app
