from flask import request
from flask_restx import Resource, Namespace
from app.dao.models.director import DirectorSchema
from container import director_service

director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        data = request.json
        directors = director_service.get_all(data)
        return directors_schema.dump(directors), 200


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):

    def get(self, director_id):
        director = director_service.get_one(director_id)
        return director_schema.dump(director), 200
