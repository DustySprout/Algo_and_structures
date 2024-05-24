import unittest
from os import name

from src.FiniteState import *


class TestFiniteStateSearch(unittest.TestCase):

    def test1_pattern_is_found(self):
        fa = finite_state_search("aaa", "aaapaaa")
        self.assertEqual(fa, [0, 4])

    def test_empty_string(self):
        fa = finite_state_search("", "an")
        self.assertEqual(fa, [])

    def test_same_pattern_and_string(self):
        fa = finite_state_search("abc", "abc")
        self.assertEqual(fa, [0])


if name == "main":
    unittest.main()
