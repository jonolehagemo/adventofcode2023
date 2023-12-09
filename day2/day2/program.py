def get_file_content(filepath):
    with open(filepath) as filehandle:
        return filehandle.readlines()


def process1(lines):
    threshold = {'red': 12, 'green': 13, 'blue': 14}
    result: int = 0

    for line in lines:
        ok = True
        (game_id, data_string) = line[4:].strip().split(': ')

        for handful in data_string.split('; '):
            for cube in handful.split(', '):
                (value, key) = cube.split(' ')
                if threshold[key] < int(value):
                    ok = False

        if ok:
            result += int(game_id)

    return result


def process2(lines):
    result: int = 0

    for line in lines:
        removed_game = line[4:].strip()
        (game_id, data_string) = removed_game.split(': ')
        line_sums = {'red': 1, 'green': 1, 'blue': 1}
        for handful in data_string.split('; '):
            for cube in handful.split(', '):
                (value, key) = cube.split(' ')
                if line_sums[key] < int(value):
                    line_sums[key] = int(value)

        line_power = line_sums['red'] * line_sums['green'] * line_sums['blue']

        result += line_power

    return result


if __name__ == '__main__':
    print(process1(get_file_content('input.txt')))
    print(process2(get_file_content('input.txt')))
