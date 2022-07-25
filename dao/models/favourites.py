from marshmallow import Schema, fields
from application.setup_db import db
from application.dao.models.base import BaseModel


class Favourites(BaseModel):
    __tablename__ = 'favourites'
    """Модель класса избранного."""

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"), nullable=False)


class FavouritesSchema(Schema):
    """Схема для сериализации класса избранного."""

    id = fields.Int()
    user_id = fields.Int()
    movie_id = fields.Int()
