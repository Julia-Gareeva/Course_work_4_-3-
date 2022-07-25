from marshmallow import Schema, fields
from application.setup_db import db
from application.dao.models.base import BaseModel


class Movie(BaseModel):
    __tablename__ = 'movies'
    """Модель класса фильмы."""

    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    trailer = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"), nullable=False)
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("directors.id"), nullable=False)
    director = db.relationship("Director")


class MovieSchema(Schema):
    """Схема для сериализации класса фильмы."""
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
