from application.dao.base import BaseDAO
from application.dao.models.users import User
from application.dao.models.auth import AuthSchema


class AuthDAO(BaseDAO):
    """Объект доступа к данным для auth модели."""

    def create(self, email, password_hash) -> AuthSchema:
        """Метод для создания нового пользователя."""
        new_user = User(
            email=email,
            password_hash=password_hash,
        )
        self.session.add(new_user)
        self.session.commit()

        return AuthSchema().dump(new_user)

    def get_user_by_email(self, email: str):
        """Метод для получения пользователей с определенным email."""
        user = self.session.query(User).filter(User.email == email).one_or_none()

        if user is not None:
            return AuthSchema().dump(user)

        return None

    def get_user_by_id(self, id: int):
        """Метод возвращающий пользователя с заданным ID."""
        users = self.session.query(User).filter(User.id == id).one_or_none()

        if users is not None:
            return AuthSchema().dump(users)
        return None
