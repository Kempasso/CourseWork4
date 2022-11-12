from paginate_sqlalchemy import SqlalchemyOrmPage

from app.dao.models import Movie
from sqlalchemy import desc


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self, page=None, status=None):
        query = self.session.query(Movie).order_by(desc(status))
        if page:
            result = SqlalchemyOrmPage(query, page=int(page), items_per_page=12)
            return result
        return query.all()

    def get_one(self, movie_id):
        return self.session.query(Movie).get(movie_id)
