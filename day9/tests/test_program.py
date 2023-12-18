import pytest

from day9.day9.program import get_input, process, extrapolate


def test_get_input():
    assert get_input("input1.txt") == [[0, 3, 6, 9, 12, 15], [1, 3, 6, 10, 15, 21], [10, 13, 16, 21, 30, 45]]


def test_extrapolate():
    assert extrapolate([0, 3, 6, 9, 12, 15]) == [-3, 0, 3, 6, 9, 12, 15, 18]


@pytest.mark.parametrize("index,expected", [
    (-1, 114),
    (0, 2),
])
def test_process(index, expected):
    assert process(get_input("input1.txt"), index) == expected
