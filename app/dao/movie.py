from app.dao.models import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        result = self.session.query(Movie).all()
        return result

    def get_one(self, movie_id):
        return self.session.query(Movie).get(movie_id)

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, movie_id):
        movie = self.get_one(movie_id)
        self.session.delete(movie)
        self.session.commit()
