def get_input(filepath: str) -> list[tuple[str, int]]:
    with open(filepath) as filehandle:
        return [(line.split()[0], int(line.split()[1].strip())) for line in filehandle.readlines()]


def get_card_value(card: str, deck: str) -> int:
    return {card: 10 ** index for index, card in enumerate(deck)}.get(card, 0)


def get_hand_value(hand: str, deck: str) -> [int]:
    return [get_card_value(card, deck) for card in hand]


def get_group(hand: str) -> dict[str, int]:
    return {card: hand.count(card) for card in hand}


def get_rank_value(hand: str) -> int:
    return sum([10 ** (value - 1) for value in get_group(hand).values()])


def get_best_hand(hand: str, deck: str) -> str:
    if "J" not in hand:
        return hand

    possible_hands = [hand.replace("J", sub) for sub in list(set(hand) - set("J")) + list(deck[-1])]
    ranking = [[get_rank_value(hand), get_hand_value(hand, deck), hand] for hand in set(possible_hands)]
    ranking.sort()

    return ranking[-1][-1]


def process(lines, deck):
    indexed = []

    for (hand, bid) in lines:
        best_hand = get_best_hand(hand, deck) if deck[0] == 'J' else hand
        indexed.append([get_rank_value(best_hand), get_hand_value(hand, deck), best_hand, hand, bid])

    indexed.sort()
    return sum([index * rank[4] for index, rank in enumerate(indexed, start=1)])


if __name__ == '__main__':
    data = get_input('input.txt')
    print(process(data, "23456789TJQKA"))
    print(process(data, "J23456789TQKA"))
