from flask import request
from flask_restx import Resource, Namespace
from app.dao.models.genre import GenreSchema
from app.helpers.decorators import auth_required, admin_required
from container import genre_service

genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200

    def post(self):
        data = request.json
        new_genre = genre_service.create(data)
        return genre_schema.dump(new_genre), 201


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):

    @auth_required
    def get(self, genre_id):
        genre = genre_service.get_one(genre_id)
        return genre_schema.dump(genre), 200

    @admin_required
    def put(self, genre_id):
        data = request.json
        data['id'] = genre_id
        genre_service.update(data)
        return 'Успешное изменение', 200

    @admin_required
    def delete(self, genre_id):
        genre_service.delete(genre_id)
        return 'Успешное удаление', 200
