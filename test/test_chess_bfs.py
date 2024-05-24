import unittest
from chess_bfs import *


class TestBFSShortMinesPath(unittest.TestCase):
    def test_normal_case(self):
        find_shortest_safe_route("test.input.txt", "test.output.txt")
        with open('test.output.txt', 'r') as file:
            first_line = file.readline()
            numbers = first_line.split()

        self.assertEqual(int(numbers[0]),12)

    def test_empty_input(self):
        find_shortest_safe_route("test.input.txt", "test.output.txt")
        with open('test.output.txt', 'r') as file:
            first_line = file.readline()
            numbers = first_line.split()
        self.assertEqual(int(numbers[0]), -1)
