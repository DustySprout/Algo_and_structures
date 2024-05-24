import unittest
from ChessBFS import *


class TestBFSShortMinesPath(unittest.TestCase):
    def test_normal_case(self):
        find_shortest_safe_route("./resources/input.txt", "./resources/output.txt")
        with open('./resources/output.txt', 'r') as file:
            first_line = file.readline()
            numbers = first_line.split()

        self.assertEqual(int(numbers[0]),12)

    def test_empty_input(self):
        find_shortest_safe_route("./resources/input_empty.txt", "./resources/output_empty.txt")
        with open('./resources/output_empty.txt', 'r') as file:
            first_line = file.readline()
            numbers = first_line.split()
        self.assertEqual(int(numbers[0]), -1)
