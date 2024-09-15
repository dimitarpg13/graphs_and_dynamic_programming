import unittest
from toposort.toposort import topological_sort


class TopoSortTestCase(unittest.TestCase):

    def test_toposort(self):
        num_nodes = 4
        edges = [[0, 1], [1, 2], [3, 1], [3, 2]]
        adj = [[] for _ in range(num_nodes)]

        for i in edges:
            adj[i[0]].append(i[1])

        topo = topological_sort(adj, num_nodes)
        self.assertListEqual([3, 0, 1, 2], topo)
