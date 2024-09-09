import sys


class DijkstraIEFD:
    """
    Iteratively Expanding Front of Distances Algorithm (IEFD)
    """
    def __init__(self, vertex_count, adjacency_matrix):
        self.vertex_count = vertex_count
        self.adjacency_matrix = adjacency_matrix

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def min_distance(self, dist, spt_set):

        # Initialize minimum distance for next node
        min_dist = sys.maxsize
        min_index = -1
        # Search nearest vertex not in the shortest path tree
        for k in range(self.vertex_count):
            if dist[k] < min_dist and spt_set[k] is False:
                min_dist = dist[k]
                min_index = k

        return min_index

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def run(self, s):
        """
        Run Dijkstra's algorithm obtaining shortest paths from a given starting element with index s
        :param s: start index
        :return: list of shortest path lengths
        """
        dist = [sys.maxsize] * self.vertex_count
        dist[s] = 0
        spt_set = [False] * self.vertex_count

        for _ in range(self.vertex_count):

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
            for y in range(self.vertex_count):
                if self.adjacency_matrix[x][y] > 0 and spt_set[y] is False and \
                        dist[y] > dist[x] + self.adjacency_matrix[x][y]:
                    dist[y] = dist[x] + self.adjacency_matrix[x][y]

        return dist


import heapq

# iPair ==> Integer Pair
iPair = tuple


class DijkstraIEDFOpt:
    """
    Iteratively Expanding Distance Front Optimized Algorithm (IEDFOpt)
    """
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adjacency_matrix = [[] for _ in range(vertex_count)]

    def addEdge(self, u: int, v: int, w: int):
        self.adjacency_matrix[u].append((v, w))
        self.adjacency_matrix[v].append((u, w))

    def run(self, t):
        """
        Computes the shortest paths from t to all other nodes
        :param t: initial node
        :return: list of distances from t to all other nodes
        """
        # vector for the distances and initialize the distance of t
        dist = [sys.maxsize] * self.vertex_count
        dist[t] = 0

        # priority queue storing vertices that are being preprocessed
        pq = []
        heapq.heappush(pq, (0, t))


class DijkstraDP:
    """
    Dijsktra's algorithm implemented via Dynamic Programming
    """
    def __init__(self, vertex_count, adjacency_matrix):
        self.vertex_count = vertex_count
        self.adjacency_matrix = adjacency_matrix
        self.dist = [sys.maxsize] * self.vertex_count
        self.dist[vertex_count] = 0
