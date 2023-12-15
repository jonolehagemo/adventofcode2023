import unittest

from day6.day6 import program


class MyTestCase(unittest.TestCase):
    def test_process1(self):
        tuples = program.get_file_content1('input1.txt')
        result: int = program.process(tuples)
        self.assertEqual(288, result)  # add assertion here

    def test_get_file_content2(self):
        tuples = program.get_file_content2('input1.txt')
        self.assertEqual(list((71530, 940200)), tuples)  # add assertion here

    def test_process2(self):
        lines = program.get_file_content2('input1.txt')
        result: int = program.process(lines)
        self.assertEqual(71503, result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
