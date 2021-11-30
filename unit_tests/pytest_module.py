# first
# pip install -U pytest
# pytest --version
# to run test
# pytest unit_tests/pytest_module.py


def sum_numbers(x, y):
    return x + y


def test_sum_numbers():
    assert sum_numbers(3, 4) == 7
