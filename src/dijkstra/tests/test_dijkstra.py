import unittest
from dijkstra.dijkstra import DijkstraNaive


class DijkstraTestCase(unittest.TestCase):

    def test_dijkstra_naive_impl(self):
        g = DijkstraNaive(9)
        g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                   [4, 0, 8, 0, 0, 0, 0, 11, 0],
                   [0, 8, 0, 7, 0, 4, 0, 0, 2],
                   [0, 0, 7, 0, 9, 14, 0, 0, 0],
                   [0, 0, 0, 9, 0, 10, 0, 0, 0],
                   [0, 0, 4, 14, 10, 0, 2, 0, 0],
                   [0, 0, 0, 0, 0, 2, 0, 1, 6],
                   [8, 11, 0, 0, 0, 0, 1, 0, 7],
                   [0, 0, 2, 0, 0, 0, 6, 7, 0]
                   ]
        dist = g.run(0)
        print(dist)
        self.assertEqual(dist[0], 0)  # add assertion here
        self.assertEqual(dist[1], 4)
        self.assertEqual(dist[7], 8)


if __name__ == '__main__':
    unittest.main()
