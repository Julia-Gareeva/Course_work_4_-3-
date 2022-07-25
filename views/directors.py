from flask_restx import Resource, Namespace
from application.dao.models.directors import DirectorSchema
from application.implemented import director_service

director_ns = Namespace('directors')


"""Представления для сущности режиссеров /directors/."""
@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        """Метод для получения всех режиссеров."""
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200


"""Представления для сущности режиссеров /directors/<int:rid>."""
@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    def get(self, rid):
        """Метод для получения одного режиссера по его ID."""
        r = director_service.get_one(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200
