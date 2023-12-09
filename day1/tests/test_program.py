import unittest
from day1.day1 import program


class MyTestCase(unittest.TestCase):
    def test_get_file_content(self):
        for filepath, expected_lines in {'input1.txt': 4, 'input2.txt': 7}.items():
            result = program.get_file_content(filepath)
            self.assertEqual(len(result), expected_lines)

    def test_process1(self):
        lines: list[str] = program.get_file_content('input1.txt')
        result: int = program.process(lines, program.find_first1, program.find_last1)
        self.assertEqual(result, 142)  # add assertion here

    def test_process2(self):
        lines: list[str] = program.get_file_content('input2.txt')
        result: int = program.process(lines, program.find_first2, program.find_last2)
        self.assertEqual(result, 281)  # add assertion here


if __name__ == '__main__':
    unittest.main()
