import pytest

from day8.day8.program import get_input, process


def test_get_input():
    (directions, network) = get_input("input1.txt")
    assert directions == "RL"
    assert network == {'AAA': ('BBB', 'CCC'),
                       'BBB': ('DDD', 'EEE'),
                       'CCC': ('ZZZ', 'GGG'),
                       'DDD': ('DDD', 'DDD'),
                       'EEE': ('EEE', 'EEE'),
                       'GGG': ('GGG', 'GGG'),
                       'ZZZ': ('ZZZ', 'ZZZ')}


@pytest.mark.parametrize("filepath,expected", [
    ('input1.txt', 2),
    ('input2.txt', 6),
    ('task1.txt', 12169),
])
def test_process(filepath, expected):
    (instructions, graph) = get_input(filepath)
    result = process(instructions, graph, (lambda n: n == 'AAA'), (lambda n: n == 'ZZZ'))
    assert result == expected
