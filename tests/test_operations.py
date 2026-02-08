import pytest
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (10, 5, 5),
    (0, 5, -5),
    (-3, -2, -1),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (3, 4, 12),
    (-2, 5, -10),
    (0, 100, 0),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5),
    (-9, 3, -3),
    (0, 1, 0),
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
