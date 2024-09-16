import unittest
from dfs.dfs import DepthFirstSearchRecursive


class DepthFirstSearchTestCase(unittest.TestCase):
    def test_dfs(self):
        adj_list = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], []]
        dfs = DepthFirstSearchRecursive(adj_list)
        dfs_list = dfs.run()
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
