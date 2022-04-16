import pytest
from shapes import Rectangle, Square


@pytest.fixture
def example_rectangle():
    return Rectangle(width=2, height=4)

def test_rectangle_init():
    r = Rectangle(width=2, height=4)
    assert r.width == 2
    assert r.height == 4
    assert r.get_area(2, 4) == 8

def test_perimeter_rectangle():
    p = Rectangle(4, 6)
    assert p.get_perimeter(4, 6) == 10

def test_square():
    s = Square(5)
    assert s.get_area() == 25









