import unittest
import random

from src.zigzag_traversal import zigzag_traversal


class TestZigzagTraversal(unittest.TestCase):
    def test_zigzag_traversal(self):
        m, n = 3, 5
        matrix = [[random.randint(1, 100) for _ in range(n)] for _ in range(m)]
        print("Generated Matrix:")
        for row in matrix:
            print(row)

        traversal_result = zigzag_traversal(matrix)
        print("\nTraversal Result:")
        print(traversal_result)


if __name__ == '__main__':
    unittest.main()
