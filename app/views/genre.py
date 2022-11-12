from flask import request
from flask_restx import Resource, Namespace
from app.dao.models.genre import GenreSchema
from container import genre_service

genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        data = request.json
        genres = genre_service.get_all(data)
        return genres_schema.dump(genres), 200


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):

    def get(self, genre_id):
        genre = genre_service.get_one(genre_id)
        return genre_schema.dump(genre), 200
