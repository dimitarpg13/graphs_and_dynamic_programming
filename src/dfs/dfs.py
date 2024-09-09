import sys


class DepthFirstSearchUndirectedGraph:
    def __init__(self, adj):
        """
        The undirected graph is given as an adjacency list
        :param adj: adjacency list
        """
        self.adj = adj

    def visit_recursive(self, start, visited, visitations):
        visited[start] = True
        visitations.append(start)
        for i in self.adj[start]:
            if not visited[i]:
                self.visit_recursive(i, visited, visitations)

    def run(self):
        visitations = []
        visited = [False] * len(self.adj)
        self.visit_recursive(0, visited, visitations)
        return visitations
