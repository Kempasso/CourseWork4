class MovieService:
    def __init__(self, dao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, movie_id):
        return self.dao.get_one(movie_id)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        movie_id = data.get('id')
        movie = self.get_one(movie_id)
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')
        self.dao.update(movie)

    def delete(self, movie_id):
        return self.dao.delete(movie_id)
