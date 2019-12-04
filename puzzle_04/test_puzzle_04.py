import pytest
from puzzle_04 import is_password_valid, is_password_strictly_valid


def test_int_to_digits():
    pass


@pytest.mark.parametrize(
    "password, is_valid",
    [
        (222222, True),
        (2222222, False),
        (111111, True),
        (223450, False),
        (123789, False),
        (145678, False),
    ],
)
def test_is_password_valid(password, is_valid):
    assert is_password_valid(password) == is_valid


@pytest.mark.parametrize(
    "password, is_valid",
    [
        (222222, False),
        (2222222, False),
        (111111, False),
        (223450, False),
        (123789, False),
        (145678, False),
        (123444, False),
        (111122, True),
        (112233, True),
    ],
)
def test_is_password_strictly_valid(password, is_valid):
    assert is_password_strictly_valid(password) == is_valid
