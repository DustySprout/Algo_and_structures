import unittest
from kruskala import Graph
import csv


class TestGraph(unittest.TestCase):

    def test_add_edge(self):
        graph = Graph(4)
        with open('test.islands.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for i, row in enumerate(reader):
                for j, weight in enumerate(row):
                    if weight != '0':
                        graph.add_edge(i, j, int(weight))
        self.assertEqual(len(graph.edges), 15)

    def test_find(self):
        graph = Graph(4)
        with open('test.islands.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for i, row in enumerate(reader):
                for j, weight in enumerate(row):
                    if weight != '0':
                        graph.add_edge(i, j, int(weight))
        parent = [0, 1, 2, 3, 4]
        self.assertEqual(graph.find(parent, 0), 0)

    def test_union(self):
        graph = Graph(4)
        with open('test.islands.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for i, row in enumerate(reader):
                for j, weight in enumerate(row):
                    if weight != '0':
                        graph.add_edge(i, j, int(weight))
        parent = [1, 1, 2, 3, 4]
        rank = [0, 0, 0, 0, 0]
        graph.apply_union(parent, rank, 0, 1)
        self.assertEqual(parent, [1, 1, 2, 3, 4])

    def test_kryskala(self):
        graph = Graph(4)
        with open('test.islands.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for i, row in enumerate(reader):
                for j, weight in enumerate(row):
                    if weight != '0':
                        graph.add_edge(i, j, int(weight))
        result = graph.kryskala()
        self.assertEqual(len(result), 3)


if __name__ == '__main__':
    unittest.main()
