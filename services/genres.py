from application.services.base import BaseService


class GenreService(BaseService):
    """Класс с бизнес-логикой сущности жанры."""

    def get_one(self, bid):
        """Метод для получения одного жанра по ID."""
        return self.dao.get_one(bid)

    def get_all(self):
        """Метод для получения всех жанров."""
        return self.dao.get_all()

    def create(self, genre_d):
        """Метод для создания нового жанра."""
        return self.dao.create(genre_d)

    def update(self, genre_d):
        """Метод для обновления одного жанра."""
        self.dao.update(genre_d)
        return self.dao

    def delete(self, rid):
        """Метод для удаления одного фильма."""
        self.dao.delete(rid)
