import time
import pytest
from main.service.user import UserService


@pytest.fixture(autouse=True, scope='session')
def time_1():
    print(f"start test  {time.ctime()}")
    yield
    print(f"end test  {time.ctime()}")


class TestUserService:
    @pytest.fixture(autouse=True)
    def user_service(self, user_dao):
        self.user_service = UserService(dao=user_dao)

    def test_user_by_name(self):
        user = self.user_service.get_by_user_name('test')
        assert user is not None
        assert len(user) >= 0

    def test_get_all(self):
        user = self.user_service.get_all()
        assert user is not None
        assert len(user) == 2
