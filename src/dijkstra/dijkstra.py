import sys


class DijkstraNaive:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)]
                      for _ in range(vertices)]

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def min_distance(self, dist, spt_set):

        # Initialize minimum distance for next node
        min_dist = sys.maxsize
        min_index = -1
        # Search nearest vertex not in the shortest path tree
        for k in range(self.V):
            if dist[k] < min_dist and spt_set[k] == False:
                min_dist = dist[k]
                min_index = k

        return min_index

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def run(self, t):

        dist = [sys.maxsize] * self.V
        dist[t] = 0
        spt_set = [False] * self.V

        for _ in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to t in first iteration
            x = self.min_distance(dist, spt_set)

            # Put the minimum distance vertex in the
            # shortest path tree
            spt_set[x] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for y in range(self.V):
                if self.graph[x][y] > 0 and spt_set[y] == False and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]

            return dist
