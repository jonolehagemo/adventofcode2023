from functools import reduce


def get_file_content1(filepath) -> list[tuple[int, int]]:
    with open(filepath) as filehandle:
        lines = filehandle.readlines()
        return list(zip(map(lambda x: int(x), lines[0].strip().split()[1:]),
                        map(lambda x: int(x), lines[1].strip().split()[1:])))


def get_file_content2(filepath) -> list[tuple[int, int]]:
    with open(filepath) as filehandle:
        lines = filehandle.readlines()
        return list(zip(map(lambda x: int(x), lines[0].replace(" ", "").strip().split(":")[1:]),
                        map(lambda x: int(x), lines[1].replace(" ", "").strip().split(":")[1:])))


def count_wins(time, distance):
    count = 0

    for x in range(1, time):
        if ((time - (time - x)) * (time - x)) > distance:
            count += 1

    return count


def process(tuples):
    return reduce(lambda x, y: x * y, map(lambda x: count_wins(x[0], x[1]), tuples), 1)


if __name__ == '__main__':
    print(process(get_file_content1('input.txt')))
    print(process(get_file_content2('input.txt')))

# 293046
# 35150181
