from itertools import pairwise


def get_input(filepath: str) -> list[[int]]:
    with open(filepath) as filehandle:
        return [list(map(int, line.split())) for line in filehandle.read().split("\n")]


def extrapolate(values: list[int]) -> list[int]:
    if not any(values):
        return [0, *values, 0]
    subs = extrapolate([right - left for left, right in pairwise(values)])
    return [values[0] - subs[0], *values, values[-1] + subs[-1]]


def process(data: list[list[int]], index: int) -> int:
    return sum([extrapolate(ints)[index] for ints in data])


if __name__ == '__main__':
    data1 = get_input('input.txt')
    print(process(data1, 0))
    print(process(data1, -1))
