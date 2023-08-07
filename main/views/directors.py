from flask_restx import Resource, Namespace
from flask import request
from main.dao.model.director import DirectorSchema
from main.helpers.decorators import auth_required, auth_admin
from main.implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    # @auth_required
    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        data = request.json
        director_service.create(data)
        return "Ok", 201


@director_ns.route('/<int:rid>/')
class DirectorView(Resource):
    def get(self, rid):
        r = director_service.get_one(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    def put(self, rid):
        data = request.json
        data['id'] = rid
        director_service.update(data)
        return "ok", 204

    def delete(self, rid):
        director_service.delete(rid)
        return 'ok', 204
