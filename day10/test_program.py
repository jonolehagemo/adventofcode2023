import pytest

from day10.program import process, Maze, Runner


def test_maze_init():
    maze = Maze("input1.txt")
    assert maze.graph == {
        (0, 0): '-', (0, 1): 'L', (0, 2): '|', (0, 3): 'F', (0, 4): '7',
        (1, 0): '7', (1, 1): 'S', (1, 2): '-', (1, 3): '7', (1, 4): '|',
        (2, 0): 'L', (2, 1): '|', (2, 2): '7', (2, 3): '|', (2, 4): '|',
        (3, 0): '-', (3, 1): 'L', (3, 2): '-', (3, 3): 'J', (3, 4): '|',
        (4, 0): 'L', (4, 1): '|', (4, 2): '-', (4, 3): 'J', (4, 4): 'F'
    }


@pytest.mark.parametrize("filepath,coordinate,expected", [
    ("input1.txt", (-1, -1), ((1, 1), 'F', {0: 1, 3: 2})),
    ("input1.txt", (1, 1), ((1, 1), 'F', {0: 1, 3: 2})),
    ("input1.txt", (0, 0), ((0, 0), '-', {1: 3, 3: 1})),
    ("input1.txt", (0, 1), ((0, 1), 'L', {2: 1, 3: 0})),
])
def test_maze_get_tile(filepath, coordinate, expected):
    ((expected_row_index, expected_column_index), expected_tile, expected_directions) = expected
    maze = Maze(filepath)
    ((row_index, column_index), tile, directions) = maze.get_tile(coordinate)
    assert row_index == expected_row_index
    assert column_index == expected_column_index
    assert tile == expected_tile
    assert directions == expected_directions


@pytest.mark.parametrize("filepath,expected", [
    ("input1.txt", ((1, 1), 'F', 1)),
])
def test_runner_init(filepath, expected):
    maze = Maze(filepath)
    ((row_index, column_index), tile, directions) = maze.get_start()
    runner = Runner(_maze=maze, _coordinate=(row_index, column_index), _tile=tile, _outbound_direction=directions[0])
    print(f"runner: {runner}")
    ((r_row_index, r_column_index), r_tile, r_outbound_direction) = runner.steps[0]
    ((expected_row_index, expected_column_index), expected_tile, expected_directions) = expected
    assert r_row_index == expected_row_index
    assert r_column_index == expected_column_index
    assert r_tile == expected_tile
    assert r_outbound_direction == expected_directions


@pytest.mark.parametrize("filepath,expected", [
    ("input1.txt", ((1, 2), '-', 1)),
])
def test_runner_move_next(filepath, expected):
    maze = Maze(filepath)
    ((row_index, column_index), tile, directions) = maze.get_start()
    runner = Runner(maze, (row_index, column_index), tile, directions[0])
    runner.move_next()
    ((r_row_index, r_column_index), r_tile, r_outbound_direction) = runner.steps[-1]
    ((expected_row_index, expected_column_index), expected_tile, expected_directions) = expected
    assert r_row_index == expected_row_index
    assert r_column_index == expected_column_index
    assert r_tile == expected_tile
    assert r_outbound_direction == expected_directions


@pytest.mark.parametrize("filepath,expected,count", [
    ("input1.txt", ((2, 1), '|', 0), 8),
])
def test_runner_find_loop(filepath, expected, count):
    maze = Maze(filepath)
    ((row_index, column_index), tile, directions) = maze.get_start()
    runner = Runner(maze, (row_index, column_index), tile, directions[0])
    print(f"runner: {runner.steps}")
    ((r_row_index, r_column_index), r_tile, r_outbound_direction) = runner.steps[-1]
    ((expected_row_index, expected_column_index), expected_tile, expected_directions) = expected
    assert r_row_index == expected_row_index
    assert r_column_index == expected_column_index
    assert r_tile == expected_tile
    assert r_outbound_direction == expected_directions
    assert len(runner.steps) == count


@pytest.mark.parametrize("filepath,expected", [
    ("input1.txt", 4),
    #    ("input2.txt", 8),
])
def test_process(filepath, expected):
    assert process(filepath) == expected
