from application.dao.models.movies import Movie
from application.dao.base import BaseDAO


# CRUD - это набор операций: создание, чтение, обновление и удаление.
class MovieDAO(BaseDAO):
    """Объект доступа к данным для movie модели."""

    def get_one(self, bid):
        """Метод для получения одного фильма по ID."""
        return self.session.query(Movie).get(bid)

    def get_all(self):
        """Метод для получения всех фильмов."""
        # А еще можно сделать так, вместо всех методов get_by_*
        # t = self.session.query(Movie)
        # if "director_id" in filters:
        #     t = t.filter(Movie.director_id == filters.get("director_id"))
        # if "genre_id" in filters:
        #     t = t.filter(Movie.genre_id == filters.get("genre_id"))
        # if "year" in filters:
        #     t = t.filter(Movie.year == filters.get("year"))
        # return t.all()
        return self.session.query(Movie).all()

    def get_by_director_id(self, val):
        """Метод для получения фильмов с определенным режиссером по запросу типа /movies/?director_id=24."""
        return self.session.query(Movie).filter(Movie.director_id == val).all()

    def get_by_genre_id(self, val):
        """Метод для получения фильмов с определенным жанром по запросу типа /movies/?genre_id=5."""
        return self.session.query(Movie).filter(Movie.genre_id == val).all()

    def get_by_year(self, val):
        """Метод для получения фильмов за определенный год по запросу типа /movies/?year=2008."""
        return self.session.query(Movie).filter(Movie.year == val).all()

    def create(self, movie_d):
        """Метод для создания/добавления одного фильма."""
        ent = Movie(**movie_d)
        self.session.add(ent)
        self.session.commit()
        self.session.close()

    def delete(self, rid):
        """Метод для удаления одного фильма."""
        movie = self.get_one(rid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_d):
        """Метод для обновления одного фильма."""
        movie = self.get_one(movie_d.get("id"))
        movie.title = movie_d.get("title")
        movie.description = movie_d.get("description")
        movie.trailer = movie_d.get("trailer")
        movie.year = movie_d.get("year")
        movie.rating = movie_d.get("rating")
        movie.genre_id = movie_d.get("genre_id")
        movie.director_id = movie_d.get("director_id")

        self.session.add(movie)
        self.session.commit()
        self.session.close()

    def sort_date_up(self):
        """Метод для сортировки фильмов по дате, вывод на экран самых последних фильмов."""
        return self.session.query(Movie).order_by(Movie.year.desc())

    def sort_date_down(self):
        """Метод для сортировки фильмов по дате, вывод на экран с самых первых строк."""
        return self.session.query(Movie).order_by(Movie.year)

