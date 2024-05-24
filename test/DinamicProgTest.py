from DinamicProg import *
import unittest


class TestIndianaJones(unittest.TestCase):
    def test_case(self):
        row_size, col_size, sneaky_way = read_input("DinamicProg.in")
        result = ijones_traversal(sneaky_way, rows=row_size, cols=col_size)
        out_put = read_output("DinamicProg.out")
        self.assertEqual(result, out_put)


def read_output(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read().strip()  # Remove any leading/trailing whitespace
        if not data:
            raise ValueError("file.out порожній")
        try:
            return int(data)
        except ValueError as e:
            raise ValueError(f"Invalid data in output file: {e}")


if __name__ == "__main__":
    unittest.main()
