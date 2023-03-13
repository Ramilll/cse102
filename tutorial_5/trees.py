import math


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def size(root: Node):
    "returns the size of the tree"
    if root is None:
        return 0
    return 1 + size(root.left) + size(root.right)  # type: ignore


def sum_values(root: Node):
    "returns the sum of all values in the tree"
    if root is None:
        return 0
    return root.value + sum_values(root.left) + sum_values(root.right)  # type: ignore


def height(root: Node) -> int:
    "computes the height of the tree"
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))  # type: ignore


def mirrored(left_root: Node, right_root: Node):
    if (left_root, right_root) == (None, None):
        return True
    if (left_root == None) != (right_root == None):
        return False
    flag1 = left_root.value == right_root.value
    flag2 = mirrored(left_root.left, right_root.right)  # type: ignore
    flag3 = mirrored(left_root.right, right_root.left)  # type: ignore
    return flag1 and flag2 and flag3


def check_symmetry(root: Node):
    if root is None:
        return True
    return mirrored(root.left, root.right)  # type: ignore


def check_BST(root: Node, min_val=float("-inf"), max_val=float("inf")) -> bool:
    eps = 1e-3
    if root is None:
        return True
    if root.value < min_val or root.value > max_val:
        return False
    left_valid = check_BST(root.left, min_val, root.value - eps)  # type: ignore
    right_valid = check_BST(root.right, root.value + eps, max_val)  # type: ignore
    return left_valid and right_valid


def min_BST(root: Node):
    if root == None:
        return math.inf
    if root.left == None:
        return root.value
    return min_BST(root.left)


def in_order_traversal(root: Node):
    if root == None:
        return []
    return in_order_traversal(root.left) + [root.value] + in_order_traversal(root.right)  # type: ignore


def min_diff(root: Node):
    arr = in_order_traversal(root)
    differences = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
    if len(differences) == 0:
        return math.inf
    return min(differences)
