from flask import request
from flask_restx import Resource, Namespace
from app.dao.models.movie import MovieSchema
from container import movie_service

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        data = request.json
        movies = movie_service.get_all(data)
        return movies_schema.dump(movies), 200


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):

    def get(self, movie_id):
        movie = movie_service.get_one(movie_id)
        return movie_schema.dump(movie), 200
