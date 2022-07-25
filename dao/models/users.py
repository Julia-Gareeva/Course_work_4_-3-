from marshmallow import Schema, fields
from application.setup_db import db
from application.dao.models.base import BaseModel
from application.dao.models.genres import Genre


class User(BaseModel):
    __tablename__ = 'users'
    """Модель класса пользователей."""

    email = db.Column(db.String(200), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(150))
    age = db.Column(db.Integer, db.CheckConstraint("age > 16"))
    favourite_genre = db.Column(db.ForeignKey(Genre.name))
    genre = db.relationship("Genre")


class UserSchema(Schema):
    """Схема для сериализации класса пользователей."""
    id = fields.Int()
    email = fields.Str()
    password_hash = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    age = fields.Int()
    favourite_genre = fields.Int()
