import unittest

from day5.day5 import program
from day5.day5.program import get_file_content


class MyTestCase(unittest.TestCase):
    def test_get_file_content(self):
        (seeds, maps) = get_file_content('input1.txt')
        expected_seeds = list([79, 14, 55, 13])
        self.assertEqual(expected_seeds, seeds)
        self.assertEqual(7, len(maps))

    def test_process1(self):
        lines: list[str] = program.get_file_content('input1.txt')
        result: int = program.process1(lines)
        self.assertEqual(13, result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
