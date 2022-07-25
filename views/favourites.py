from flask import request
from flask_restx import Resource, Namespace
from application.dao.models.favourites import Favourites
from application.dao.models.favourites import FavouritesSchema
from application.helpers.decorators import auth_required
from application.implemented import favourites_service

favo_ns = Namespace('favourites')


"""Представления для сущности фильмы /favourites/movies/."""
@favo_ns.route('/movies/')
class FavouritesView(Resource):
    @auth_required
    def get(self):
        """Метод для получения всех фильмов в списке избранного."""
        page = int(request.args.get('page'))

        all_movies = favourites_service.get_all()[12*(page-1):12*page]
        res = FavouritesSchema(many=True).dump(all_movies)
        return res, 200


"""Представления для сущности фильмы /favourites/movies/<int:fid>."""
@favo_ns.route('/movies/<int:fid>/')
class FavouritesOneView(Resource):
    @auth_required
    def get(self, fid: int):
        """Метод для получения одного фильма из списка Избранного по ID."""
        b = favourites_service.get_one(fid)
        sm_d = FavouritesSchema().dump(b)
        return sm_d, 200

    @auth_required
    def post(self, fid: int):
        """Метод для добавления фильма в список Избранного."""
        req_json = request.json(fid)
        favourites_service.adding_favourites(req_json)
        return "", 201, {"location": f"/movies/{Favourites.id}"}

    @auth_required
    def delete(self, fid: int):
        """Метод для удаления фильма из списка Избранного."""
        favourites_service.delete_from_favourites(fid)
        return "", 204
