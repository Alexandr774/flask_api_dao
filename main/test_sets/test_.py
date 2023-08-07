import pytest

test = [(1, 2, 3), (3, 4, 7), (2, 4, 6)]


def sum_num(a, b):
    return a + b


@pytest.mark.parametrize('number', test)
def test_set(number):
    assert sum_num(number[0], number[1]) == number[2]


def test_num(number_42):
    assert number_42[1] + number_42[0] == 43


@pytest.mark.skip(reason='ok')
def test_num_1(number_42):
    assert number_42 == 42
