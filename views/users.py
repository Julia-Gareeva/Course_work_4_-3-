from flask import request
from flask_restx import Resource, Namespace
from application.dao.models.users import UserSchema
from application.helpers.decorators import auth_required, myself_required
from application.implemented import user_service

user_ns = Namespace('users')


"""Представления для сущности пользователи /users/."""
@user_ns.route('/')
class UserView(Resource):
    def get(self):
        """Метод для получения всех пользователей по запросу типа /users/."""
        users = user_service.get_all()
        response = UserSchema(many=True).dump(users)
        return response, 200


"""Представления для сущности пользователи /users/<int:uid>."""
@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid: int):
        """Метод для получения одного пользователя по его ID."""
        try:
            user = user_service.get_one(uid)
            result = UserSchema().dump(user)
            return result, 200
        except Exception as ex:
            return ex, 404

    @auth_required
    @myself_required
    def patch(self, uid):
        """Метод для частичного изменения одного пользователя."""
        data = request.get_json()
        user_service.update_part(data, uid)
        return '', 204

    @auth_required
    @myself_required
    def delete(self, uid: int):
        """Метод для удаления одного пользователя по его ID."""
        user_service.delete(uid)
        return '', 204


@user_ns.route('/password/')
class UserPasswordView(Resource):
    @auth_required
    @myself_required
    def put(self, uid):
        """Метод для изменения пароля пользователя."""
        data = request.get_json()
        return user_service.update_password(data, uid)
