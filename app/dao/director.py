from app.dao.models import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_one(self, director_id):
        return self.session.query(Director).get(director_id)

    def create(self, data):
        director = Director(**data)
        self.session.add(director)
        self.session.commit()
        return director

    def update(self, director):
        self.session.add(director)
        self.session.commit()
        return director

    def delete(self, director_id):
        director = self.get_one(director_id)
        self.session.delete(director)
        self.session.commit()
