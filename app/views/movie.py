from flask import request
from flask_restx import Resource, Namespace
from app.dao.models.movie import MovieSchema
from app.helpers.decorators import auth_required, admin_required
from container import movie_service

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):

    @auth_required
    def get(self):
        movies = movie_service.get_all()
        return movies_schema.dump(movies), 200

    @admin_required
    def post(self):
        data = request.json
        new_movie = movie_service.create(data)
        return movie_schema.dump(new_movie), 201


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):

    @auth_required
    def get(self, movie_id):
        movie = movie_service.get_one(movie_id)
        return movie_schema.dump(movie), 200

    @admin_required
    def put(self, movie_id):
        data = request.json
        data['id'] = movie_id
        movie_service.update(data)
        return 'Успешное изменение', 200

    @admin_required
    def delete(self, movie_id):
        movie_service.delete(movie_id)
        return 'Успешное удаление', 200
