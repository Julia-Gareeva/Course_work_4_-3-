from marshmallow import Schema, fields, validates, ValidationError
import re


class AuthSchema(Schema):
    """Схема для сериализации аутентификации."""

    email = fields.Str(required=True)
    password_hash = fields.Str(required=True)


class AuthRegisterRequest(Schema):
    """Схема для сериализации регистрации."""

    email = fields.Str(required=True)
    password_hash = fields.Str(required=True)

    """Возникает, когда пароль недействителен."""
    @staticmethod
    @validates("email")
    def validate_email(email):
        if len(email) <= 0:
            raise ValidationError("Количество символов должно быть больше 0.")
        if len(email) > 200:
            raise ValidationError("Количество символов должно быть не больше 200 символов.")

        item = ["@", ".", "com" or "ru"]
        for el in item:
            if el not in email:
                raise ValidationError("Email должен содержать такие символы: '@', '.', 'com' или 'ru'.")

    # Проверяет наличие символов в обоих регистрах,
    # чисел, спецсимволов и минимальную длину 8 символов
    pattern1 = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    # Проверяет наличие символов в обоих регистрах,
    # числел и минимальную длину 8 символов
    pattern2 = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'

    @staticmethod
    @validates("password_hash")
    def validate_password_hash(password_hash, pattern1, pattern2):
        if len(password_hash) <= 0:
            raise ValidationError("Количество символов должно быть больше 0.")
        if len(password_hash) > 200:
            raise ValidationError("Количество символов должно быть не больше 200 символов.")
        if len(password_hash) < 8:
            raise ValidationError("Пароль должен состоять не менее чем из 8 символов.")

        """Валидация пароля по регулярному выражению."""
        if re.match(password_hash, pattern1, pattern2) is None:
            raise ValidationError('Пароль имеет неправильный формат.')
