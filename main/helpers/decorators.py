import jwt
from flask import request
from flask_restx import abort
from main.helpers.constans import JWT_SECRET, JWT_ALGORITHM


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers
        a = data['Authorization'].split('Bearer ')[-1]
        try:
            jwt.decode(a, JWT_SECRET, algorithms=JWT_ALGORITHM)
        except Exception:
            print('no token access')
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def auth_admin(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers
        a = data['Authorization'].split('Bearer ')[-1]
        try:
            p = jwt.decode(a, JWT_SECRET, algorithms=JWT_ALGORITHM)
            if p['role'] == 'admin':
                return func(*args, **kwargs)
        except Exception:
            print('no token access')
            abort(401)
        return abort(401)

    return wrapper
