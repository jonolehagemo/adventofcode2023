from functools import reduce


def get_file_content(filepath):
    with open(filepath) as filehandle:
        return filehandle.readlines()


def get_stats(lines):
    result = list()

    for index, line in enumerate(lines):
        numbers = line.strip().split(': ')[1].replace('| ', '').replace('  ', ' ').split()
        matching_numbers_count = len(numbers) - len(set(numbers))
        points = 2 ** (matching_numbers_count - 1) if matching_numbers_count > 0 else 0
        result.append((index, matching_numbers_count, points))

    return result


def process1(lines):
    return reduce(lambda x, y: x + y, map(lambda x: x[2], get_stats(lines)))


def flatten_list(nested_list):
    # check if list is empty
    if not (bool(nested_list)):
        return nested_list

    # to check instance of list is empty or not
    if isinstance(nested_list[0], list):
        # call function with sublist as argument
        return flatten_list(*nested_list[:1]) + flatten_list(nested_list[1:])

    # call function with sublist as argument
    return nested_list[:1] + flatten_list(nested_list[1:])


def get_copies(stats, stat):
    result = 0
    (index, matching_numbers_count, points) = stat
    copies = stats[index + 1:index + matching_numbers_count + 1]
    sub_copies = list()
    if len(copies):
        for copy in copies:
            sub_copies.append(get_copies(stats, copy))

    return copies + sub_copies


def process2(lines):
    result = 0
    stats = get_stats(lines)

    for stat in stats:
        result += 1 + len(flatten_list(get_copies(stats, stat)))

    return result


if __name__ == '__main__':
    print(process1(get_file_content('input.txt')))
    print(process2(get_file_content('input.txt')))
