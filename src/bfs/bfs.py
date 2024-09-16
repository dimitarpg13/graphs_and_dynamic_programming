from collections import deque


class BreadthFirstSearch:
    """
    Breadth First Search using deque
    """
    def __init__(self, adj_list, num_nodes):
        """
        :param adj_list: adjacency list
        :param num_nodes: number of nodes
        """
        self.adj_list = adj_list
        self.num_nodes = num_nodes
        self.visited = [False] * self.num_nodes

    def run(self, start):
        q = deque()

        self.visited[start] = True
        q.append(start)
        stack = []
        while q:
            current = q.popleft()
            stack.append(current)
            print(current)
            for v in self.adj_list[current]:
                if v and not self.visited[v]:
                    self.visited[v] = True
                    q.append(v)

        return stack


if __name__ == '__main__':
    adj_list = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], []]
    num_nodes = 6
    bfs = BreadthFirstSearch(adj_list, num_nodes)
    res = bfs.run(0)
    print(res)


