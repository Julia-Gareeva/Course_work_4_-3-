from unittest.mock import MagicMock
import pytest
from application.dao.users import UserDAO
from application.dao.models.users import User
from application.services.auth import AuthService


@pytest.fixture()
def auth():
    auth_dao = UserDAO(None)

    
