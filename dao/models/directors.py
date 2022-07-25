from marshmallow import Schema, fields
from application.setup_db import db
from application.dao.models.base import BaseModel


class Director(BaseModel):
    __tablename__ = 'directors'
    """Модель класса режиссеров."""

    name = db.Column(db.String(200), unique=True, nullable=False)


class DirectorSchema(Schema):
    """Схема для сериализации класса режиссеров."""
    id = fields.Int()
    name = fields.Str()
