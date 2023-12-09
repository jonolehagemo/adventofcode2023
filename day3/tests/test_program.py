import unittest

from day3.day3 import program
from program import get_border_coordinates


class MyTestCase(unittest.TestCase):
    def test_process1(self):
        lines: list[str] = program.get_file_content('input1.txt')
        result: int = program.process1(lines)
        self.assertEqual(4361, result)  # add assertion here

    def test_get_border_coordinates(self):
        coordinate = (1, 4, 4)
        result = get_border_coordinates(coordinate)
        self.assertEqual(tuple(), result)

    def test_process2(self):
        lines: list[str] = program.get_file_content('input1.txt')
        result: int = program.process2(lines)
        self.assertEqual(467835, result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
