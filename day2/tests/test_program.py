import unittest

from day2.day2 import program


class MyTestCase(unittest.TestCase):
    def test_process1(self):
        lines: list[str] = program.get_file_content('input1.txt')
        result: int = program.process1(lines)
        self.assertEqual(8, result)  # add assertion here

    def test_process2(self):
        lines: list[str] = program.get_file_content('input2.txt')
        result: int = program.process2(lines)
        self.assertEqual(2286, result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
