import unittest
from dijkstra.dijkstra import DijkstraIEDF


class DijkstraTestCase(unittest.TestCase):

    def test_dijkstra_naive_impl(self):

        adj_matr = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                   [4, 0, 8, 0, 0, 0, 0, 11, 0],
                   [0, 8, 0, 7, 0, 4, 0, 0, 2],
                   [0, 0, 7, 0, 9, 14, 0, 0, 0],
                   [0, 0, 0, 9, 0, 10, 0, 0, 0],
                   [0, 0, 4, 14, 10, 0, 2, 0, 0],
                   [0, 0, 0, 0, 0, 2, 0, 1, 6],
                   [8, 11, 0, 0, 0, 0, 1, 0, 7],
                   [0, 0, 2, 0, 0, 0, 6, 7, 0]]

        g = DijkstraIEDF(9,adj_matr)

        dist = g.run(0)

        self.assertEqual(dist[0], 0)  # add assertion here
        self.assertEqual(dist[1], 4)
        self.assertEqual(dist[2], 12)
        self.assertEqual(dist[3], 19)
        self.assertEqual(dist[4], 21)
        self.assertEqual(dist[5], 11)
        self.assertEqual(dist[6], 9)
        self.assertEqual(dist[7], 8)
        self.assertEqual(dist[8], 14)


if __name__ == '__main__':
    unittest.main()
