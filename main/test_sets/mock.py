from unittest.mock import MagicMock
import pytest
from main.dao.user import UserDAO
from main.service.user import UserService

# class ProdClass:
#     def m1(self):
#         print("m1")
#
#     def m2(self):
#         print('m2')
#
#
# if __name__ == '__main__':
#     pc = ProdClass()
#     # pc.m1 = MagicMock(return_value='123')
#     # print(pc.m1())
#
#     pc.m2 = MagicMock(side_effect=Exception('oh oh'))
#     pc.m2()
user_dao = UserDAO(None)

user_dao.get_by_name = MagicMock(return_value="test")
user_service = UserService(user_dao)


def test_user():
    assert user_service.get_by_user_name('test') == 'test'
