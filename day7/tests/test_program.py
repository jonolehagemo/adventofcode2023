import pytest

from day7.day7 import program


@pytest.mark.parametrize("card,expected", [
    ('J', 0),
    ('2', 1),
    ('3', 10),
    ('A', 100),
])
def test_get_card_value(card, expected):
    assert program.get_card_value(card, "23A") == expected


@pytest.mark.parametrize("hand,expected", [
    ('XXXXX', [0, 0, 0, 0, 0]),
    ('22222', [1, 1, 1, 1, 1]),
    ('33322', [10, 10, 10, 1, 1]),
    ('23456', [1, 10, 100, 1000, 10000]),
])
def test_get_cards_value(hand, expected):
    deck = "23456789TJQKA"
    assert program.get_hand_value(hand, deck) == expected


@pytest.mark.parametrize("cards,expected", [
    ('23456', {'2': 1, '3': 1, '4': 1, '5': 1, '6': 1}),
    ('22345', {'2': 2, '3': 1, '4': 1, '5': 1}),
    ('22234', {'2': 3, '3': 1, '4': 1}),
    ('22223', {'2': 4, '3': 1}),
    ('22222', {'2': 5}),
])
def test_get_group(cards, expected):
    assert program.get_group(cards) == expected


@pytest.mark.parametrize("cards,expected", [
    ('23456', 5),
    ('22345', 13),
    ('22234', 102),
    ('22223', 1001),
    ('22222', 10000),
])
def test_get_group_value(cards, expected):
    assert program.get_rank_value(cards) == expected


@pytest.mark.parametrize("cards,expected", [
    ('32T3K', '32T3K'),
    ('T55J5', 'T5555'),
    ('KK677', 'KK677'),
    ('KTJJT', 'KTTTT'),
    ('QQQJA', 'QQQQA'),
    ('QQJAA', 'QQAAA'),
    ('JQQAA', 'AQQAA'),
    ('7JJK7', '777K7')

])
def test_best_cards(cards, expected):
    deck = "J23456789TQKA"
    best_cards = program.get_best_hand(cards, deck)
    assert best_cards == expected


@pytest.mark.parametrize("deck,expected", [
    ("23456789TJQKA", 6440),
    ("J23456789TQKA", 5905),
])
def test_process_with_test_input(deck, expected):
    lines = [('32T3K', 765), ('KK677', 28), ('T55J5', 684), ('QQQJA', 483), ('KTJJT', 220)]
    result: int = program.process(lines, deck)
    assert result == expected


@pytest.mark.parametrize("deck,expected", [
    ("23456789TJQKA", 248453531),
    ("J23456789TQKA", 248781813),
])
def test_process_with_solution_input(deck, expected):
    lines = program.get_input("input.txt")
    result: int = program.process(lines, deck)
    assert result == expected
