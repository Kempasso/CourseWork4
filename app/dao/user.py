from app.dao.models import User


class UserDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self):
        users = self.session.query(User).all()
        return users

    def get_one(self, user_id):
        user = self.session.query(User).get(user_id)
        return user

    def create(self, user):
        with self.session.begin():
            self.session.add(user)

    def update(self, user):
        self.session.add(user)
        self.session.commit()

    def get_by_username(self, username):
        user = self.session.query(User).filter(User.username == username).first()
        return user
