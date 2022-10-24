from flask import request
from flask_restx import Resource, Namespace
from app.dao.models.director import DirectorSchema
from app.helpers.decorators import admin_required, auth_required
from container import director_service

director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        directors = director_service.get_all()
        return directors_schema.dump(directors), 200

    @admin_required
    def post(self):
        data = request.json
        new_director = director_service.create(data)
        return director_schema.dump(new_director), 201


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):

    @auth_required
    def get(self, director_id):
        director = director_service.get_one(director_id)
        return director_schema.dump(director), 200

    @admin_required
    def put(self, director_id):
        data = request.json
        data['id'] = director_id
        director_service.update(data)
        return 'Успешное изменение', 200

    @admin_required
    def delete(self, director_id):
        director_service.delete(director_id)
        return 'Успешное удаление', 200
