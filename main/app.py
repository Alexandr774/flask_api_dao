from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from config import Config
from dao.model.user import User
from setup_db import db
from views.auth import auth_ns
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.user import user_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.app_context().push()
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    cors = CORS()
    cors.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


def create_data(app):
    user = User(username="root_update", password="random_password", role='admin', name='qwert',
                surname='1234', favorite_genre=2)

    with app.app_context():
        db.create_all()

    with db.session.begin():
        db.session.add_all({user})


if __name__ == '__main__':
    app = create_app(Config())
    # create_data(app)
    app.run(port=5000)
