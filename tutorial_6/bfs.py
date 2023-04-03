import math
from collections import deque


def shortest_route_len(G, s, t):
    distances = {i: math.inf for i in range(len(G))}
    distances[s] = 0
    queue = deque([(s, 0)])

    while queue:
        node, distance = queue.popleft()
        if node == t:
            return distance
        for neighbor in G[node]:
            if distances[neighbor] == math.inf:
                distances[neighbor] = distance + 1
                queue.append((neighbor, distance + 1))

    return math.inf
