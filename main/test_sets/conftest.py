import pytest
import time


@pytest.fixture()
def number_42():
    return 42, 1


@pytest.fixture(autouse=True, scope='session')
def time_1():
    print("start test")
    yield
    print(' end test ')

#
# @pytest.fixture(autouse=True, scope='function')
# def time_2():
#     yield
#     print('test is Ok')
#
#
# @pytest.fixture(autouse=True, scope='module')
# def time_3():
#     yield
#     print('test is Ok')
#
#
# @pytest.fixture(autouse=True, scope='class')
# def time_4():
#     yield
#     print(f'test is Ok {time.strftime("%d %b %x ")}')
