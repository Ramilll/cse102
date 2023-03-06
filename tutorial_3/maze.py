from typing import List


def is_open(m, n, i, j):
    return 0 <= i < n and 0 <= j < n and m[i][j] == 1


def maze(m: List[List[int]], n: int, i: int, j: int):
    """Generates a path from position (i, j) to (n - 1, n - 1) in a maze

    Args:
        m (List[List[int]]): maze matrix in which 1 represents open space and 0 represents a wall
        n (int): size of the maze
        i (int): the row of the starting position
        j (int): the column of the starting position
    """
    if i == n - 1 and j == n - 1:
        return [(i, j)]

    if j < n - 1 and is_open(m, n, i, j + 1):
        right_path = maze(m, n, i, j + 1)
        if right_path:
            return [(i, j)] + right_path

    if i < n - 1 and is_open(m, n, i + 1, j):
        down_path = maze(m, n, i + 1, j)
        if down_path:
            return [(i, j)] + down_path

    return None
