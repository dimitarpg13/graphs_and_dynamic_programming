import unittest
from dfs.dfs import DepthFirstSearchRecursive
from utils.utils import arc_list_to_adj_list


class DepthFirstSearchTestCase(unittest.TestCase):
    def test_dfs_ex1(self):
        arc_list = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
        num_nodes = 6
        adj_list = arc_list_to_adj_list(arc_list, num_nodes)
        dfs = DepthFirstSearchRecursive(adj_list, num_nodes)
        dfs_list = dfs.run(0)
        self.assertListEqual([0, 1, 2, 3, 4, 5], dfs_list)  # add assertion here

    def test_dfs_ex2(self):
        arc_list = [[0, 1], [1, 2], [3, 1], [3, 2]]
        num_nodes = 4
        adj_list = arc_list_to_adj_list(arc_list, num_nodes)
        dfs = DepthFirstSearchRecursive(adj_list, num_nodes)
        dfs_list = dfs.run(3)
        self.assertListEqual([3, 1, 2], dfs_list)


if __name__ == '__main__':
    unittest.main()
