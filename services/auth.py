from flask_restx import abort
from application.services.base import BaseService
from application.dao.auth import AuthDAO
from application.dao.models.auth import AuthSchema
from application.helpers.constants import SECRET_KEY, PWD_HASH_SALT, PWD_HASH_ITERATIONS, ALGORITM
import hashlib
import base64
import hmac
import datetime
import jwt


class AuthService(BaseService[AuthDAO]):
    """Метод для генерации хеша пароля."""
    @staticmethod
    def get_hash(password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            ALGORITM,
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_password(self, password_hash, other_password) -> bool:
        """Метод для сравнения паролей."""
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac(
                ALGORITM,
                other_password,  # Преобразовываем пароль в байты
                PWD_HASH_SALT,
                PWD_HASH_ITERATIONS
            ))

    def generate_tokens(self, user: AuthSchema, is_refresh=False):
        """Метод для генерации токенов."""
        if not is_refresh:
            raise Exception()

        payload = {
            'email': user['email'],
            'id': user['id'],
            'exp': datetime.utcnow() + datetime.timedelta(minutes=30)
        }
        # Генерируем access токен на 30 минут
        access_token = jwt.encode(
            payload=payload,
            key=SECRET_KEY,
            algoritm=ALGORITM
        )

        payload['exp'] = datetime.utcnow() + datetime.timedelta(days=130)
        # Генерируем refresh токен на 130 дней
        refresh_token = jwt.encode(
            payload=payload,
            key=SECRET_KEY,
            algoritm=ALGORITM
        )
        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def registers(self, email, password) -> AuthSchema:
        """Метод для регистрации пользователя."""
        password_hash = self.get_hash(password)
        return self.dao.create(email, password_hash)

    def login(self, email: str, password_hash: str) -> dict[str | str]:
        """Метод для того чтобы пользователь залогинился."""
        try:
            user = self.dao.get_user_by_email(email=email)
            password_hash = self.get_hash(password_hash)
            compare = self.compare_password(password_hash, password_hash)
            if compare:
                return self.generate_tokens(user, is_refresh=True)
        except Exception():
            print("Неизвестная ошибка.")

    def get_user_by_email(self, email):
        """Метод для получения пользователя по email"""
        return self.dao.get_user_by_email(email)

    def get_user_by_id(self, id: int):
        """Метод возвращающий пользователя с заданным ID."""
        return self.dao.get_user_by_id(id)

    def approve_refresh_token(self, email: str, id: int, access_token, refresh_token):
        """Метод для генерации access и refresh токена"""
        tokens_1 = self.get_user_by_email(email)
        tokens_2 = self.get_user_by_id(id)
        if not tokens_1 and tokens_2:
            raise abort(404)

        data = jwt.decode(jwt=[access_token, refresh_token], key=SECRET_KEY, algorithms=[ALGORITM])
        id = data['id']
        result = self.generate_tokens(id, None, is_refresh=True)
        return result
