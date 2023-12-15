def create_seeds(parts):
    return [int(x) for x in parts[0].split(':')[1].strip().split()]


def create_maps(parts):
    result = dict()
    for part in parts[1:]:
        category, coordinates_string = part.split(" map:\n")
        source_category, destination_category = category.split("-to-")
        coordinates_lines = list(coordinates_string.split("\n"))

        coordinates = list()

        for coordinates_line in coordinates_lines:
            destination_range_start, source_range_start, range_length = coordinates_line.split(" ")
            coordinates.append((destination_range_start, source_range_start, range_length))

        result[(source_category, destination_category)] = coordinates

    return result


def get_file_content(filepath):
    with open(filepath) as filehandle:
        parts = filehandle.read().split("\n\n")
        seeds = create_seeds(parts)
        print(seeds)
        maps = create_maps(parts)
        print(maps)
        return seeds, maps


def process1(lines):
    return 0


if __name__ == '__main__':
    print(process1(get_file_content('input.txt')))
