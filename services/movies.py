from application.services.base import BaseService


class MovieService(BaseService):
    """Класс с бизнес-логикой сущности фильмы."""

    def get_one(self, bid):
        """Метод для получения одного фильма по ID."""
        return self.dao.get_one(bid)

    def get_all(self, filters):
        """Метод для получения всех фильмов.
        Метод для получения фильмов с определенным режиссером по запросу типа /movies/?director_id=24.
        Метод для получения фильмов с определенным жанром по запросу типа /movies/?genre_id=5.
        Метод для получения фильмов за определенный год по запросу типа /movies/?year=2008."""
        if filters.get("director_id") is not None:
            movies = self.dao.get_by_director_id(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = self.dao.get_by_genre_id(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = self.dao.get_by_year(filters.get("year"))
        else:
            movies = self.dao.get_all()
        return movies

    def create(self, movie_d):
        """Метод для создания нового фильма."""
        return self.dao.create(movie_d)

    def update(self, movie_d):
        """Метод для обновления одного фильма."""
        self.dao.update(movie_d)
        return self.dao

    def delete(self, rid):
        """Метод для удаления одного фильма."""
        self.dao.delete(rid)
