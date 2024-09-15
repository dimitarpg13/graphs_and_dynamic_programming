def topological_sort_helper(v, adj, visited, stack):
    # Mark the current node as visited
    visited[v] = True

    # Recur for all adjacent vertices
    for i in adj[v]:
        if not visited[i]:
            topological_sort_helper(i, adj, visited, stack)

    # Push current vertex to stack which stores the result
    stack.append(v)


# Function to perform Topological Sort
def topological_sort(adj, num_nodes):
    # Stack to store the result
    stack = []

    visited = [False] * num_nodes

    # Call the recursive helper function to store
    # Topological Sort starting from all vertices one by
    # one
    for i in range(num_nodes):
        if not visited[i]:
            topological_sort_helper(i, adj, visited, stack)

    return stack
