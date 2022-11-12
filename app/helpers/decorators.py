import jwt
from flask import request, abort

from app.helpers.constants import JWT_ALGORITHM, JWT_SECRET


def auth_required(func):
    def wrapper(*args, **kwargs):
        if not 'Authorization' in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        try:
            token_info = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        except Exception as e:
            print('JWT Exception', e)
            abort(401)
        else:
            user_id = token_info['id']
            return func(*args, **kwargs, user_id=user_id)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if not 'Authorization' in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        role = None

        try:
            user = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
            role = user.get('role', 'user')
        except Exception as e:
            print('JWT Exception', e)
            abort(401)
        if role != 'admin':
            abort(403)
        return func(*args, **kwargs)

    return wrapper
