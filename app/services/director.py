from paginate_sqlalchemy import SqlalchemyOrmPage


class DirectorService:
    def __init__(self, dao):
        self.dao = dao

    def get_all(self, data):

        return self.dao.get_all()

    def get_one(self, director_id):
        return self.dao.get_one(director_id)
