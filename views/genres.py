from flask_restx import Resource, Namespace
from application.dao.models.genres import GenreSchema
from application.implemented import genre_service

genre_ns = Namespace('genres')


"""Представления для сущности жанры /genres/."""
@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        """Метод для получения всех жанров."""
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200


"""Представления для сущности жанры /genres/<int:rid>."""
@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    def get(self, rid):
        """Метод для получения одного жанра по его ID."""
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200
