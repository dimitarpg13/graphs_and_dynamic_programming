import unittest
from toposort.toposort import topological_sort
from utils.utils import arc_list_to_adj_list

class TopoSortTestCase(unittest.TestCase):

    def test_toposort(self):
        num_nodes = 4
        arcs_list = [[0, 1], [1, 2], [3, 1], [3, 2]]
        adj_list = arc_list_to_adj_list(arcs_list, num_nodes)
        topo = topological_sort(adj_list, num_nodes)
        self.assertListEqual([3, 0, 1, 2], topo)
