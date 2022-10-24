from flask import Flask

from app.config import Config
from app.views.auth import auth_ns
from app.views.director import director_ns
from app.views.genre import genre_ns
from app.views.movie import movie_ns
from app.views.user import user_ns
from database import db
from flask_restx import Api


def create_app(config: Config):
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


def configure_app(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(user_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    api.add_namespace(auth_ns)


def create_tables():
    db.create_all()


if __name__ == '__main__':
    configs = Config()
    app = create_app(configs)
    configure_app(app)
    create_tables()
    app.run(debug=True)
