from functools import reduce


def get_file_content(filepath):
    with open(filepath) as filehandle:
        return filehandle.readlines()


# task 1
def find_first1(line):
    return line[0] if line[0].isdigit() else find_first1(line[1:])


def find_last1(line):
    return line[-1] if line[-1].isdigit() else find_last1(line[:-1])


# task 2
def get_mapping():
    return {
        'one': '1', 'two': '2', 'three': '3',
        'four': '4', 'five': '5', 'six': '6',
        'seven': '7', 'eight': '8', 'nine': '9'
    }


def find_first2(line):
    if line[0].isdigit():
        return line[0]

    for key, value in get_mapping().items():
        if line.startswith(key):
            return value

    return find_first2(line[1:])


def find_last2(line):
    if line[-1].isdigit():
        return line[-1]

    for key, value in get_mapping().items():
        if line.endswith(key):
            return value

    return find_last2(line[:-1])


def process(lines, first_func, last_func):
    return reduce(lambda x, y: x + y, map(lambda line: int(first_func(line) + last_func(line)), lines))


if __name__ == '__main__':
    print(process(get_file_content('input.txt'), find_first1, find_last1))
    print(process(get_file_content('input.txt'), find_first2, find_last2))
