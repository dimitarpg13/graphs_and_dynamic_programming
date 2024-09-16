import sys


class DepthFirstSearchRecursive:
    """
    This is the algorithm applicable both for undirected graphs and digraphs
    """
    def __init__(self, adj_list: list[list[int]], num_nodes: int):
        """
        The undirected graph is given as an adjacency list
        :param adj_list: adjacency list
        """
        self.adj_list = adj_list
        self.num_nodes = num_nodes

    def visit_recursive(self, start, visited, visitations):
        visited[start] = True
        visitations.append(start)
        for v in self.adj_list[start]:
            if not visited[v]:
                self.visit_recursive(v, visited, visitations)

    def run(self, start):
        visitations = []
        visited = [False] * self.num_nodes
        self.visit_recursive(start, visited, visitations)
        return visitations
