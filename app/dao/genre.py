from paginate_sqlalchemy import SqlalchemyOrmPage

from app.dao.models import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self, page=None):
        query = self.session.query(Genre)
        if page:
            result = SqlalchemyOrmPage(query, page=int(page), items_per_page=12)
            return result
        return query.all()

    def get_one(self, genre_id):
        return self.session.query(Genre).get(genre_id)
