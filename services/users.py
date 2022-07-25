from application.dao.models.users import User
from application.services.base import BaseService


class UserService(BaseService):
    """Класс с бизнес-логикой сущности пользователи."""

    def get_one(self, uid):
        """Метод для получения одного пользователя по его ID."""
        return self.dao.get_one(uid)

    def get_user_by_email(self, email):
        """Метод для получения пользователя по email"""
        return self.dao.get_user_by_email(email)

    def get_all(self):
        """Метод для получения всех пользователей по запросу типа /users/."""
        return self.dao.get_all()

    def delete(self, uid):
        """Метод для удаления одного пользователя."""
        self.dao.delete(uid)

    def update_password(self, user_data, uid):
        """Метод для обновления пароля одного пользователя."""
        a: User = self.get_one(uid)

        if a:
            if a.password_hash == self.get_hash(user_data.get('password_1')):
                print("Пароль старый проверку прошел.")
                user_data['password_2'] = self.get_hash(user_data.get('password_2'))
                self.dao.update_password(user_data, uid)
            else:
                print("Пароль неверный.")

            a = self.get_one(uid)
            return {"name": a.name,
                    "surname": a.surname,
                    "password_hash": str(a.password_hash)}

    def update_part(self, data, user_d):
        """Метод для частичного обновления пользователя."""
        return self.dao.update_part(data, user_d)
