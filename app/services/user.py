import base64
import hashlib
import hmac

from app.dao.models import User
from app.helpers.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:

    def __init__(self, dao):
        self.dao = dao

    def get_one(self, user_id):
        user = self.dao.get_one(user_id)
        return user

    def create(self, data):
        data['password'] = self.get_hash(data['password'])
        user = User(**data)
        self.dao.create(user)

    def update(self, data):
        user_id = data.get('id')
        user = self.get_one(user_id)
        for i in data.items():
            setattr(user, i[0], i[1])
        self.dao.update(user)

    def get_by_email(self, email):
        user = self.dao.get_by_email(email)
        return user

    def compare_password(self, hash_password, user_password):
        decoded_digest = base64.b64decode(hash_password)
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            user_password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return hmac.compare_digest(decoded_digest, hash_digest)

    def get_hash(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def change_password(self, data, user_id):
        password = data['password']
        new_password = data['new_password']
        user = self.get_one(user_id)
        if not self.compare_password(user.password, password):
            return 'Неверный пароль'
        user.password = self.get_hash(new_password)
        self.dao.update(user)
        return 'Пароль изменен'
