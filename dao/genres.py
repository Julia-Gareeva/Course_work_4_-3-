from application.dao.models.genres import Genre
from application.dao.base import BaseDAO


# CRUD - это набор операций: создание, чтение, обновление и удаление.
class GenreDAO(BaseDAO):
    """Объект доступа к данным для genre модели."""

    def get_one(self, bid):
        """Метод для получения одного жанра по ID."""
        return self.session.query(Genre).get(bid)

    def get_all(self):
        """Метод для получения всех жанров."""
        return self.session.query(Genre).all()

    def create(self, genre_d):
        """Метод для создания одного жанра."""
        ent = Genre(**genre_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        """Метод для удаления одного жанра."""
        genre = self.get_one(rid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, genre_d):
        """Метод для обновления одного жанра."""
        genre = self.get_one(genre_d.get("id"))
        genre.name = genre_d.get("name")

        self.session.add(genre)
        self.session.commit()
