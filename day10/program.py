class Maze:
    def __init__(self, _filepath):
        self.tile = "S"
        self.directions = []
        self.graph = {}
        self.directions_by_tile = {
            "L": {2: 1, 3: 0},
            "|": {0: 2, 2: 0},
            "J": {1: 0, 2: 3},
            "F": {0: 1, 3: 2},
            "7": {0: 3, 1: 2},
            "-": {1: 3, 3: 1}
        }

        with open(_filepath) as filehandle:
            for row_index, row in enumerate(filehandle.read().splitlines()):
                for column_index, col in enumerate(row):
                    self.graph[(row_index, column_index)] = col

        self.s = [coordinate for coordinate, tile in self.graph.items() if tile == 'S'][0]
        (row_index, column_index) = self.s
        # north = 0, east = 1, south = 2, west = 3
        north = True if self.graph.get((row_index - 1, column_index), ".") in ['7', '|', 'F'] else False
        east = True if self.graph.get((row_index, column_index + 1), ".") in ['J', '-', '7'] else False
        south = True if self.graph.get((row_index + 1, column_index), ".") in ['J', '|', 'L'] else False
        west = True if self.graph.get((row_index, column_index - 1), ".") in ['L', '-', 'F'] else False

        if north and east:
            self.tile = "L"
        elif north and south:
            self.tile = "|"
        elif north and west:
            self.tile = "J"
        elif south and east:
            self.tile = "F"
        elif south and west:
            self.tile = "7"
        elif east and west:
            self.tile = "-"
        else:
            self.tile = "."

    def get_start(self):
        return self.s, self.tile, list(self.directions_by_tile[self.tile].values())

    def get_tile(self, coordinate: tuple[int, int] = (-1, -1)) -> str:
        return self.graph[coordinate]


class Runner:
    def __init__(self, _maze: Maze, _coordinate: tuple[int, int], _tile: str, _outbound_direction: int):
        self.maze: Maze = _maze
        self.steps = [(_coordinate, _tile, _outbound_direction)]
        self.direction_by_from_and_tile = {
            (0, '7'): 3, (0, '|'): 0, (0, 'F'): 1,
            (1, 'J'): 0, (1, '-'): 1, (1, '7'): 2,
            (2, 'L'): 1, (2, '|'): 2, (2, 'J'): 3,
            (3, 'F'): 2, (3, '-'): 3, (3, 'L'): 0,
        }
        self.find_loop()

    def __str__(self):
        return str(self.steps)

    def get_coordinates(self):
        return self.steps[-1][0]

    def get_direction(self):
        return self.steps[-1][2]

    def get_next_coordinates(self):
        current = self.get_coordinates()

        if self.get_direction() == 0:
            return current[0] - 1, current[1] + 0

        elif self.get_direction() == 1:
            return current[0] + 0, current[1] + 1

        elif self.get_direction() == 2:
            return current[0] + 1, current[1] + 0

        else:
            return current[0] + 0, current[1] - 1

    def move_next(self):
        next_coordinates = self.get_next_coordinates()
        next_tile = self.maze.get_tile(next_coordinates)
        next_direction = self.direction_by_from_and_tile[(self.get_direction(), next_tile)]
        self.steps.append((next_coordinates, next_tile, next_direction))

    def find_loop(self):
        while self.steps[0][0] != self.get_next_coordinates():
            self.move_next()

    def get_path_length(self):
        return int(len(self.steps) / 2)


def process(_filepath: str) -> int:
    maze = Maze(_filepath)
    ((row_index, column_index), tile, directions) = maze.get_start()
    runner = Runner(maze, (row_index, column_index), tile, directions[0])

    return runner.get_path_length()


if __name__ == '__main__':
    print(process("input.txt"))
