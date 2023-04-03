def matrix_to_adjlist(M):
    """Convert a matrix to an adjacency list."""
    n = len(M)
    adjlist = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if M[i][j] == 1:
                adjlist[i].append(j)
    return adjlist


def is_symmetric(G):
    """Check if a graph is symmetric. G is an adjacency list."""
    adjacency_set = [set(neighbors) for neighbors in G]
    for i in range(len(G)):
        for j in G[i]:
            if i not in adjacency_set[j]:
                return False
    return True


def revert_edges(G):
    """Revert all edges in a graph. G is an adjacency list."""
    n = len(G)
    G_reverted = [[] for i in range(n)]
    for i in range(n):
        for j in G[i]:
            G_reverted[j].append(i)
    return G_reverted
