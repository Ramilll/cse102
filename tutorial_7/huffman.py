class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def huffman_stats(s):
    stats = {}
    for c in s:
        stats[c] = stats.get(c, 0) + 1
    for c in stats:
        stats[c] /= len(s)
    return stats
