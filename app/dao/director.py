from app.dao.models import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).order_by(Director.year).all()

    def get_one(self, director_id):
        return self.session.query(Director).get(director_id)