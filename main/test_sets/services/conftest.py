from unittest.mock import MagicMock
import pytest
from main.dao.user import UserDAO
from main.dao.model.user import User
from main.service.user import UserService


@pytest.fixture()
def user_dao():
    user_dao = UserDAO(None)
    alex = User(username='Alex', id=1, password=1234)
    alex_1 = User(username='Alex', id=2, password=1234)

    user_dao.create = MagicMock(return_value=User(id=1))
    user_dao.get_by_name = MagicMock(return_value='test')
    user_dao.get_all = MagicMock(return_value=[alex, alex_1])
    return user_dao

# b = user_dao()
# a = UserService(b)
#
# print(a.get_by_user_name('as'))
