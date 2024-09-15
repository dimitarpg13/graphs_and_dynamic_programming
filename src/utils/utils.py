

def arc_list_to_adj_list(arc_list, num_nodes):
    """
    converts arc list to adjacency list
    :param arc_list: list of arcs
      Example: [[0, 1], [1, 2], [3, 1], [3, 2]]
    :param num_nodes: number of nodes
    :return:adj_list: adjacency list
    """
    adj_list = [[] for _ in range(num_nodes)]
    for arc in arc_list:
        adj_list[arc[0]].append(arc[1])
    return adj_list


def edge_list_to_adj_list(edge_list, num_nodes):
    """
    converts edge list to adjacency list
    :param edge_list: list of arcs
      Example: [[0, 1], [1, 2], [3, 1], [3, 2]]
    :param num_nodes: number of nodes
    :return:adj_list: adjacency list
    """
    adj_list = [[] for _ in range(num_nodes)]
    for edge in edge_list:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])
    return adj_list


def adj_matrix_to_adj_list(adj_matrix, num_nodes):
    pass


def adj_list_to_adj_matrix(adj_list):
    pass