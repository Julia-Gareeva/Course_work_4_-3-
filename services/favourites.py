from application.services.base import BaseService


class FavouritesService(BaseService):
    """Класс с бизнес-логикой сущности Избранное."""

    def get_all(self):
        """Метод для получения всех фильмов в списке Избранного."""
        return self.dao.get_all()

    def get_one(self, fid):
        """Метод для получения одного фильма из списка Избранного по ID."""
        return self.dao.get_one(fid)

    def adding_favourites(self, fav):
        """Метод для добавления фильма в список Избранного."""
        return self.dao.adding_favourites(fav)

    def delete_from_favourites(self, fid):
        """Метод для удаления фильма из списка Избранного."""
        return self.dao.delete_from_favourites(fid)
