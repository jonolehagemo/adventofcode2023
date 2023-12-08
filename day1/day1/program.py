def get_file_content(filepath):
    with open(filepath) as filehandle:
        return filehandle.readlines()


# task 1
def find_first1(line):
    if line[0].isdigit():
        return line[0]

    return find_first1(line[1:])


def find_last1(line):
    if line[-1].isdigit():
        return line[-1]

    return find_last1(line[:-1])


def process1(lines):
    result: int = 0

    for line in lines:
        result += int(find_first1(line) + find_last1(line))

    return result


# task 2
mapping = {
    'one': '1', 'two': '2', 'three': '3',
    'four': '4', 'five': '5', 'six': '6',
    'seven': '7', 'eight': '8', 'nine': '9'
}


def find_first2(line):
    if line[0].isdigit():
        return line[0]

    for key, value in mapping.items():
        if line.startswith(key):
            return value

    return find_first2(line[1:])


def find_last2(line):
    if line[-1].isdigit():
        return line[-1]

    for key, value in mapping.items():
        if line.endswith(key):
            return value

    return find_last2(line[:-1])


def process2(lines):
    result: int = 0

    for line in lines:
        result += int(find_first2(line) + find_last2(line))

    return result


if __name__ == '__main__':
    print(process1(get_file_content('input.txt')))
    print(process2(get_file_content('input.txt')))
