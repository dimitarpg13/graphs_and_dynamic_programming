import unittest
from bfs.bfs import BreadthFirstSearch
from utils.utils import arc_list_to_adj_list

class BreathFirstSearchTestCase(unittest.TestCase):
    def test_bfs_ex1(self):
        arc_list = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
        num_nodes = 6
        adj_list = arc_list_to_adj_list(arc_list, num_nodes)
        bfs = BreadthFirstSearch(adj_list, num_nodes)
        bfs_list = bfs.run(0)
        self.assertListEqual([0, 1, 2, 3, 4, 5], bfs_list)  # add assertion here

    def test_bfs_ex2(self):
        arc_list = [[0, 1], [1, 2], [3, 1], [3, 2]]
        num_nodes = 4
        adj_list = arc_list_to_adj_list(arc_list, num_nodes)
        bfs = BreadthFirstSearch(adj_list, num_nodes)
        bfs_list = bfs.run(3)
        self.assertListEqual([3, 1, 2], bfs_list)


if __name__ == '__main__':
    unittest.main()
