from flask import request
from flask_restx import Resource, Namespace
from application.dao.models.auth import AuthRegisterRequest
from application.implemented import auth_service
from application.helpers.decorators import auth_required
from application.helpers.decorators import myself_required

auth_ns = Namespace('auth')


"""Представления для сущности авторизации /auth/register/."""
@auth_ns.route('/register/')
class RegisterView(Resource):
    def post(self):
        """Метод чтобы передавая email и пароль, создавался пользователя в системе."""
        data = request.json
        validated_data = AuthRegisterRequest().load(data)

        auth_service.registers(
            email=validated_data['email'],
            password=validated_data['password_hash']
        )
        return '', 200


@auth_ns.route('/login/')
class LoginView(Resource):
    def post(self):
        """Метод для создания авторизации."""
        data = request.json
        email = data.get("email", None)
        password_hash = data.get("password_hash", None)
        if None in ['email', 'password_hash']:
            return "", 400

        tokens = auth_service.login(email, password_hash)
        return tokens, 200

    @auth_required
    @myself_required
    def put(self):
        """Метод для обновления авторизации."""
        req_json = request.json
        token1 = req_json.get('access_token')
        token2 = req_json.get('refresh_token')
        tokens = auth_service.approve_refresh_token(token1, token2)
        return tokens, 201
