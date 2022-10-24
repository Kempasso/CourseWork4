from flask import request
from flask_restx import Resource, Namespace

from app.dao.models.user import UserSchema
from app.helpers.decorators import admin_required
from container import user_service

user_ns = Namespace('users')
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersView(Resource):

    @admin_required
    def get(self):
        users = user_service.get_all()
        return users_schema.dump(users), 200

    def post(self):
        data = request.json
        user_service.create(data)
        return 'Учтенная запись создана', 200


@user_ns.route('/<int:user_id>')
class UserView(Resource):

    @admin_required
    def get(self, user_id):
        user = user_service.get_one(user_id)
        return user_schema.dump(user), 200

    @admin_required
    def put(self, user_id):
        data = request.json
        data['id'] = user_id
        user_service.update(data)
        return '', 200

