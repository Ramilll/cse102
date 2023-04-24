import heapq


class Node:
    def __init__(self, value, left=None, right=None, prob=0):
        self.value = value
        self.left = left
        self.right = right
        self.prob = prob

    def __lt__(self, other):
        return self.prob < other.prob


def huffman_stats(s: str):
    stats = {}
    for c in s:
        stats[c] = stats.get(c, 0) + 1
    for c in stats:
        stats[c] /= len(s)
    return stats


def huffman_tree(d: dict):
    nodes_list = [Node(value=letter, prob=prob) for letter, prob in d.items()]
    nodes = heapq.heapify(nodes_list)
    while len(nodes_list) > 1:
        left = heapq.heappop(nodes_list)
        right = heapq.heappop(nodes_list)
        parent_node = Node(value=None, prob=left.prob + right.prob, left=left, right=right)
        heapq.heappush(nodes_list, parent_node)
    return nodes_list[0]


def traverse_a_huffman_tree(root, prefix_code="", codes={}):
    codes[root] = prefix_code
    if root.left:
        traverse_a_huffman_tree(root.left, prefix_code=prefix_code + "0", codes=codes)
    if root.right:
        traverse_a_huffman_tree(root.right, prefix_code=prefix_code + "1", codes=codes)

    return codes


def huffman_codes(root):
    node_codes = traverse_a_huffman_tree(root=root, prefix_code="")
    letter_codes = {}
    for node, code in node_codes.items():
        if node.value:
            letter_codes[node.value] = code
    return letter_codes
