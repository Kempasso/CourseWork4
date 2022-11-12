import calendar
import datetime

import jwt
from flask_restx import abort

from app.services import UserService
from app.helpers.constants import JWT_SECRET, JWT_ALGORITHM


class AuthService:

    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, email, password, is_refresh=False):
        user = self.user_service.get_by_email(email)
        if user is None:
            raise abort(404)
        if not is_refresh:
            if not self.user_service.compare_password(user.password, password):
                raise abort(400)

        data = {
            'email': user.email,
            'id': user.id
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, JWT_ALGORITHM)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, JWT_ALGORITHM)
        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(refresh_token, JWT_SECRET, JWT_ALGORITHM)
        email = data.get('email')
        return self.generate_tokens(email, None, is_refresh=True)

    def registration(self, data):
        self.user_service.create(data)

