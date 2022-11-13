from flask import request
from flask_restx import Resource, Namespace

from app.dao.models.user import UserSchema
from app.helpers.decorators import auth_required
from container import user_service

user_ns = Namespace('user')
user_schema = UserSchema()


@user_ns.route('/')
class UserView(Resource):

    @auth_required
    def get(self, user_id=None):
        user_profile = user_service.get_one(user_id)
        return user_schema.dump(user_profile), 200

    @auth_required
    def patch(self, user_id=None):
        data = request.json
        data['id'] = user_id
        user_service.update(data)
        return 'Успешно', 200


@user_ns.route('/password')
class UserPasswordView(Resource):
    @auth_required
    def put(self, user_id=None):
        data = request.json
        message = user_service.change_password(data, user_id)
        return message, 200
