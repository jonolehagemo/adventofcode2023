from itertools import pairwise


def get_input(filepath: str) -> list[[int]]:
    with open(filepath) as filehandle:
        return [list(map(int, line.split())) for line in filehandle.read().split("\n")]


def extrapolate(_values: list[int]) -> list[int]:
    if not any(_values):
        return [0, *_values, 0]
    extrapolated = extrapolate([right - left for left, right in pairwise(_values)])
    return [_values[0] - extrapolated[0], *_values, _values[-1] + extrapolated[-1]]


def process(_data: list[list[int]], index: int) -> int:
    return sum([extrapolate(ints)[index] for ints in _data])


if __name__ == '__main__':
    data = get_input('input.txt')
    print(process(data, 0))
    print(process(data, -1))
