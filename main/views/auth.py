from flask_restx import Resource, Namespace
from flask import request, abort
from main.implemented import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route('/login/')
class AuthView(Resource):
    def post(self):
        data = request.json
        return auth_service.generate_token(username=data["email"],
                                           password=data["password"])

    def put(self):
        data = request.json
        try:
            token = data["refresh_token"]
            token = auth_service.refresh_token(token)
        except Exception:
            abort(401)
        return token, 201


@auth_ns.route('/register/')
class AuthRegView(Resource):
    def post(self):
        data = request.json
        return user_service.create(data)
