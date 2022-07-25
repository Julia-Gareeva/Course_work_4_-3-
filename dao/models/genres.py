from marshmallow import Schema, fields
from application.setup_db import db
from application.dao.models.base import BaseModel


class Genre(BaseModel):
    __tablename__ = 'genres'
    """Модель класса жанров."""

    name = db.Column(db.String(200), unique=True, nullable=False)


class GenreSchema(Schema):
    """Схема для сериализации класса жанров."""
    id = fields.Int()
    name = fields.Str()
