def get_file_content(filepath):
    with open(filepath) as filehandle:
        return filehandle.readlines()


def create_data_matrix(lines):
    """
    Returns a 2d list with dot-border so we don't have take care of edge cases.
    """
    border = list('.' * (len(lines[0]) + 2))
    data = list()
    data.append(border)

    for line in lines:
        data.append(['.', *line.strip(), '.'])

    data.append(border)

    return data


def part_scan(matrix):
    result = dict()

    for i in range(len(matrix)):
        is_number = False
        start = 0
        number_string = ''

        for j in range(len(matrix[i])):
            if matrix[i][j].isdigit():
                if not is_number:
                    start = j
                    is_number = True

                if is_number:
                    number_string += matrix[i][j]

            if not matrix[i][j].isdigit():
                if is_number:
                    is_number = False
                    result[(i, start, j - 1)] = number_string
                    number_string = ''

    return result


def get_number_by_coordinate(matrix, coordinates) -> int:
    result: int = 0

    for (line, start, end), value in coordinates.items():
        sub_matrix = (*matrix[line - 1][start - 1:end + 2],
                      *matrix[line][start - 1:end + 2],
                      *matrix[line + 1][start - 1:end + 2])
        symbols = list(filter(lambda s: s not in ".0123456789", sub_matrix))

        if len(symbols):
            result += int(value)

    return result


def process1(lines):
    matrix = create_data_matrix(lines)
    return get_number_by_coordinate(matrix, part_scan(matrix))


def gear_scan(matrix):
    result = list()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '*':
                result.append((i, j, j))

    return result


def get_number_by_overlap(gear_coordinates, parts_coordinates):
    result = 0

    for gear in gear_coordinates:
        gear_border = get_border_coordinates(gear)
        part_list = list()

        for part, value in parts_coordinates.items():
            part_border = get_partnumber_coordinates(part)

            if gear_border.keys() & part_border.keys():
                part_list.append(value)

        if len(part_list) == 2:
            result += int(part_list[0]) * int(part_list[1])

    return result


def get_border_coordinates(coordinate):
    result = dict()
    (line, start, end) = coordinate

    for x in range(start - 1, end + 2, 1):
        result[(line - 1, x)] = 2
        result[(line + 1, x)] = 2

    result[(line, start - 1)] = 1
    result[(line, end + 1)] = 3

    return result


def get_partnumber_coordinates(coordinate):
    result = dict()
    (line, start, end) = coordinate

    for x in range(start, end + 1):
        result[(line, x)] = 2
        result[(line, x)] = 2

    return result


def process2(lines):
    matrix = create_data_matrix(lines)
    parts_coordinates = part_scan(matrix)
    gear_coordinates = gear_scan(matrix)
    result = get_number_by_overlap(gear_coordinates, parts_coordinates)
    return result


if __name__ == '__main__':
    print(process1(get_file_content('input.txt')))
    print(process2(get_file_content('input.txt')))
