from application.setup_db import db

from application.dao.directors import DirectorDAO
from application.dao.genres import GenreDAO
from application.dao.movies import MovieDAO
from application.dao.users import UserDAO
from application.dao.auth import AuthDAO
from application.dao.favourites import FavouritesDAO

from application.services.auth import AuthService
from application.services.users import UserService
from application.services.directors import DirectorService
from application.services.genres import GenreService
from application.services.movies import MovieService
from application.services.favourites import FavouritesService


director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
user_dao = UserDAO(session=db.session)
auth_dao = AuthDAO(session=db.session)
favourites_dao = FavouritesDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)
auth_service = AuthService(dao=auth_dao)
favourites_service = FavouritesService(dao=favourites_dao)
