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
        for i in self.adj_list[start]:
            if not visited[i]:
                self.visit_recursive(i, visited, visitations)

    def run(self):
        visitations = []
        visited = [False] * self.num_nodes
        self.visit_recursive(0, visited, visitations)
        return visitations
