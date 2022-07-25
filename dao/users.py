from application.dao.models.users import User
from application.dao.base import BaseDAO


# CRUD - это набор операций: создание, чтение, обновление и удаление.
class UserDAO(BaseDAO):
    """Объект доступа к данным для user модели."""

    def get_user_by_email(self, email: str):
        """Метод для получения пользователей с определенным email."""
        return self.session.query(User).filter(User.email == email).first()

    def get_all(self):
        """Метод для получения всех пользователей."""
        return self.session.query(User).all()

    def get_one(self, uid):
        """Метод для получения одного пользователя по его ID."""
        return self.session.query(User).get(uid)

    def delete(self, uid):
        """Метод для удаления пользователя."""
        user = self.get_one(uid)

        self.session.delete(user)
        self.session.commit()

    def update_part(self, data, uid):
        """Метод для обновления пользователя, частично."""
        user = self.get_one(uid)

        if 'email' in data:
            user.email = data.get('email')
        if 'name' in data:
            user.name = data.get('name')
        if 'surname' in data:
            user.surname = data.get('surname')
        if 'favorite_genre' in data:
            user.favorite_genre = data.get('favorite_genre')

        self.session.add(user)
        self.session.commit()
        self.session.close()

    def update_password(self, data, uid):
        """Метод для обновления пароля пользователя."""
        user = self.get_one(uid)

        if 'password_2' in data:
            user.password_hash = data.get('password_2')

        self.session.add(user)
        self.session.commit()
        self.session.close()
