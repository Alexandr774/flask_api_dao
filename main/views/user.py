import jwt
from flask_restx import Resource, Namespace

from main.helpers.constans import JWT_SECRET, JWT_ALGORITHM
from main.helpers.decorators import auth_required
from main.implemented import user_service
from main.dao.model.user import UserSchema
from flask import request

user_schema = UserSchema()
user_ns = Namespace('user')


@user_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self):
        data = request.headers
        a = data['Authorization'].split('Bearer ')[-1]
        p = jwt.decode(a, JWT_SECRET, algorithms=JWT_ALGORITHM)
        username = p['username']
        return user_schema.dump(user_service.get_by_user_name(username))

    def patch(self):
        data = request.headers
        user_up = request.json
        a = data['Authorization'].split('Bearer ')[-1]
        p = jwt.decode(a, JWT_SECRET, algorithms=JWT_ALGORITHM)
        user_up['username'] = p['username']
        print(user_up)
        user_service.update_user(user_up)
        return "ok", 204


@user_ns.route('/password/')
class UserPasView(Resource):
    def put(self):
        data = request.headers
        a = data['Authorization'].split('Bearer ')[-1]
        p = jwt.decode(a, JWT_SECRET, algorithms=JWT_ALGORITHM)
        data = request.json
        data['username'] = p['username']
        user_service.update_password(data)
        return "Ok", 201


@user_ns.route('/<name>')
class UsersView(Resource):
    def get(self, name):
        data = user_service.get_by_user_name(name)
        print(user_schema.dump(data))
        return user_schema.dump(data), 200
