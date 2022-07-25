from application.dao.base import BaseDAO
from application.dao.models.favourites import Favourites


# CRUD - это набор операций: создание, чтение, обновление и удаление.
class FavouritesDAO(BaseDAO):
    """Объект доступа к данным для favourites модели."""

    def get_all(self):
        """Метод для получения всех фильмов в списке Избранного."""
        return self.session.query(Favourites.title).all()

    def get_one(self, fid):
        """Метод для получения одного фильма из списка Избранного по ID."""
        return self.session.query(Favourites.title).get(fid)

    def adding_favorites(self, fav):
        """Метод для добавления фильма в список Избранного."""
        ent = Favourites(**fav)
        self.session.add(ent)
        self.session.commit()
        self.session.close()

    def delete_from_favourites(self, fid):
        """Метод для удаления фильма из списка Избранного."""
        movie = self.get_one(fid)
        self.session.delete(movie)
        self.session.commit()
