def revert_edges(G):
    """Revert all edges in a graph. G is an adjacency list."""
    n = len(G)
    G_reverted = [[] for i in range(n)]
    for i in range(n):
        for j in G[i]:
            G_reverted[j].append(i)
    return G_reverted


def required(G, c):
    stack = []
    stack.append(c)
    seen = set()
    while stack:
        node = stack.pop()
        seen.add(node)
        for child in G[node]:
            if child not in seen:
                stack.append(child)
    return len(seen)


def required_list(G, c):
    stack = []
    stack.append(c)
    seen = set()
    while stack:
        node = stack.pop()
        seen.add(node)
        for child in G[node]:
            if child not in seen:
                stack.append(child)
    return sorted(list(seen))


def needed_for(G, c):
    G_reverted = revert_edges(G)
    return required(G_reverted, c)
