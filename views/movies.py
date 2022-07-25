from flask import request
from flask_restx import Resource, Namespace
from application.dao.models.movies import Movie
from application.dao.models.movies import MovieSchema
from application.helpers.decorators import auth_required
from application.implemented import movie_service

movie_ns = Namespace('movies')


"""Представления для сущности фильмы /movies/."""
@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """Метод для получения всех фильмов. Постранично. А также для получения новых фильмов."""
        status = request.args.get("status")
        page = int(request.args.get('page'))
        filters = {
            "status": status
        }
        all_movies = movie_service.get_all(filters)[12*(page-1):12*page]
        res = MovieSchema(many=True).dump(all_movies)
        res['director'] = all_movies.director.name
        res['genre'] = all_movies.genre.name
        return res, 200

    @auth_required
    def post(self):
        """Метод для добавления нового фильма."""
        req_json = request.json
        movie_service.create(req_json)
        return "", 201, {"location": f"/movies/{Movie.id}"}


"""Представления для сущности фильмы /movies/<int:bid>."""
@movie_ns.route('/<int:bid>')
class MovieView(Resource):
    def get(self, bid):
        """Метод для получения одного фильма по его ID."""
        b = movie_service.get_one(bid)
        sm_d = MovieSchema().dump(b)
        sm_d['director'] = b.director.name
        sm_d['genre'] = b.genre.name
        return sm_d, 200

    @auth_required
    def put(self, bid):
        """Метод для изменения одного фильма по его ID."""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = bid
        movie_service.update(req_json)
        return "", 204

    @auth_required
    def delete(self, bid):
        """Метод для удаления одного фильма по его ID."""
        movie_service.delete(bid)
        return "", 204
