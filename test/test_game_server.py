import unittest

from src.GameServer import *


class TestGameServerLatency(unittest.TestCase):
    def test_incomplete_connections_list(self):
        find_minimum_latency_from_file("gamsrv.in", "gamsrv.out")
        with open('gamsrv.out', 'r') as file:
            first_line = file.readline()
            numbers = first_line.split()

        self.assertEqual(int(numbers[0]), 100)
