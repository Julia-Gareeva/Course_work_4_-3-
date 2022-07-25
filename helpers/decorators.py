import jwt
from flask import request, abort
from application.helpers.constants import SECRET_KEY, ALGORITM


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        try:
            jwt.decode(token, SECRET_KEY, algorithms=[ALGORITM])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        return func(*args, **kwargs)

    return wrapper


def myself_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        email = None

        try:
            user = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITM])
            email = user.get("email")
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        if email != 'email':
            abort(403)

        return func(*args, **kwargs)

    return wrapper
