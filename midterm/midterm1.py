#! /usr/bin/env python3

from typing import List, Tuple

# ====================================================================
# You must complete section I and 2 out of 3 problems in section II.

# --------------------------------------------------------------------
# You can add your tests in this function:


def _my_tests():
    pass


# --------------------------------------------------------------------
# We provide type hints for the function skeletons below. E.g.
#
# def f(x : int, y : List[int]) -> Tuple[int, int]:
#    ...
#
#   indicates that `f` is a function:
#   - that takes two arguments:
#     - `x` which is an integer, and
#     - `y` which is an array that contains integers.
#   - that returns a pair made of two integers.
#
# These annotations are ignored by Python and are provided for
# documentation purposes only.

# ====================================================================
# I. Warmup (mandatory)

# --------------------------------------------------------------------
# Given an array of integers `a` and an integer `target`, return the
# indices (as a pair) `i` & `j` such that `a[i]` and `a[j]` add up to
# `target`. Return `None` is no such indices exist.
#
# Note that the tests expect that the function returns a pair `(x, y)`
# and not a 2-element list `[x, y]`.
#
# Examples:
#   >>> two_sum([2, 7, 11, 15], 9)
#   (0, 1)
#   >>> two_sum([3, 2, 4], 6)
#   (1, 2)
#   >>> two_sum([3, 3], 6)
#   (0, 1)
#
# Test with: python3 -m unittest tests.TwoSum


def two_sum(arr: List[int], target: int) -> Tuple[int, int]:
    idx_by_number = {}
    for idx, number in enumerate(arr):
        if target - number in idx_by_number:
            zero_idx = idx_by_number[target - number]
            return (zero_idx, idx)
        idx_by_number[number] = idx
    return None  # type: ignore


# --------------------------------------------------------------------
# You are climbing a staircase. It takes `n` steps to reach the
# top. Each time you can either climb 1 or 2 steps. In how many
# distinct ways can you climb to the top?
#
# Examples:
#   >>> climb(2)
#   2
#   >>> climb(3)
#   3
#   >>> climb(10)
#   89
#
# Test with: python3 -m unittest tests.Climb


def climb(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# --------------------------------------------------------------------
# Write an algorithm to determine if a number `n` is happy.
#
# A number is happy if the following numerical sequence `u_n`
# converges to `1`:
#
# - u_0     = n
# - u_(n+1) = sum of the squares of the digits of u_n
#
# Examples:
#   >>> happy(19)
#   True
#   >>> happy(2)
#   False
#
# Test with: python3 -m unittest tests.Happy


def sum_of_squares_of_digits(n: int) -> int:
    answer = 0
    while n > 0:
        digit = n % 10
        answer += digit * digit
        n //= 10
    return answer


def happy(n: int) -> bool:
    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = sum_of_squares_of_digits(n)
    return True


# ====================================================================
# II. (Problem 1) Dynamic programming

# --------------------------------------------------------------------
# Given an integer `n`, return the least number of perfect squares
# that sum up to `n`. A perfect square is a non-negative integer that
# is the square of an integer. For example, 1, 4, 9, and 16 are
# perfect squares while 3 and 11 are not.
#
# Examples:
#   >>> perfect_square_sum(12)
#   3               # Because: 12 = 2 * 2 + 2 * 2 + 2 * 2
#   >>> perfect_square_sum(13)
#   2               # Because: 13 = 3 * 3 + 2 * 2
#
# Test with: python3 -m unittest tests.PerfectSquareSum


def perfect_square_sum(n: int) -> int:
    squares = [i * i for i in range(1, int(n**0.5) + 1)]
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        next_dp = 1e10
        for number in squares:
            if number > i:
                break
            next_dp = min(next_dp, dp[i - number] + 1)
        dp[i] = next_dp  # type: ignore
    return dp[n]


# --------------------------------------------------------------------
# We are given a check board with `m` rows and `n` columns. There is a
# cost matrix `P[i][j]` associated with square at row `i` and column
# `j`.
#
# For example, here is such a cost matrix for a board contains 4 rows
# of 5 columns each:
#
#   P = [
#     [10, 13, 47, 96,  8],
#     [11,  5, 24,  3, 41],
#     [34,  5, 12, 23,  9],
#     [ 1, 22, 12, 14, 28],
#   ]
#
# We can start at any square in the first row (row 0), and we want to
# get to anywhere in the last row `m-1` with the least total penalty,
# assuming we could only move diagonally downwards to the left,
# diagonally downwards to the right, or straight down.
#
# E.g., if we are at cell (2, 3) (2nd row 3rd column), a valid move
# can bring us to the positions:
#
#  - (3, 2) (diagonally downwards to the left),
#  - (3, 3) (straight down), or
#  - (3, 4) (diagonally downwards to the right).
#
# Write a function that takes the number `m` of rows, the number `n`
# of columns and the cost matrix and that return the least total
# penalty for traversing the board.
#
# Test with: python3 -m unittest tests.CheckBoard


def checkboard(m: int, n: int, P: List[List[int]]) -> int:
    dp = [[0] * n for _ in range(m)]
    for i in range(n):
        dp[0][i] = P[0][i]
    for i in range(1, m):
        for j in range(n):
            dp[i][j] = P[i][j] + min(
                dp[i - 1][j],
                dp[i - 1][j - 1] if j > 0 else 1e10,
                dp[i - 1][j + 1] if j < n - 1 else 1e10,
            )
    return min(dp[m - 1])


# ====================================================================
# II. (Problem 2) Discrete Interval Encoding Trees
#
# A Discrete Interval Encoding Tree} (diet) is a tree data structure
# for representing a set of integers.
#
# Specifically, a diet is a binary search tree where each node is an
# interval, represented as a pair of the form `(x, y)`
# where `x` & `y` are integers and `x <= y`.
#
# Such a node will represent the range `[x..y]`, i.e. the set
# `{x, x + 1, x + 2, ..., y}`. Note that both `x` and `y` are part
# of this set.
#
# To build the search tree constituting a diet, we use the following
# comparison `<~` on intervals:
#
#      (x, y) <~ (u, v) if y < u
#
# Every diet must satisfy a "diet invariant", which states:
#
#   Every pair of distinct nodes in the diet must have separated
#   intervals.
#
# Two intervals `(x, y)` and `(u, v)` are said to be separated if:
#
#   y + 1 < u   OR   v + 1 < x.
#
# Below is an example diet containing the set
#
#   {2, 5, 6, 7, 8, 9, 10, 13, 14}
#
#
#                        (5, 10)
#                        /     \
#                       /       \
#                    (2, 2)   (13, 14)
#
# Here is the start of a diet implementation, built out of instances
# of `DietNode`.

# --------------------------------------------------------------------
class DietNode:
    """A node of a diet"""

    # ----------------------------------------------------------------
    # DO NOT CHANGE THIS CONSTRUCTOR
    #
    # The example below can be constructed with:
    #
    # test_diet = midterm1.DietNode(
    #     lo    = 5,
    #     hi    = 10,
    #     left  = midterm1.DietNode(lo =  2, hi =  2),
    #     right = midterm1.DietNode(lo = 13, hi = 14),
    # )

    def __init__(self, lo: int, hi: int, left=None, right=None):
        self.lo = lo  # smallest number in the interval
        self.hi = hi  # biggest number in the interval
        self.left = left  # left subtree
        self.right = right  # right subtree

    # ----------------------------------------------------------------
    # Question 1
    #
    # Complete the member function `inorder()` that returns a list
    # of the numbers stored in the diet, sorted in increasing order.
    #
    # You should implement this by performing a single traversal of
    # the diet.
    #
    # Examples:
    #   >>> test_diet = ... # Diet given above
    #   >>> test_diet.inorder()
    #   [2, 5, 6, 7, 8, 9, 10, 13, 14]
    #
    # Test with: python3 -m unittest tests.Diet.test_inorder

    def inorder(self) -> List[int]:
        left, middle, right = [], [], []
        if self.left is not None:
            left = self.left.inorder()
        middle = list(range(self.lo, self.hi + 1))
        if self.right is not None:
            right = self.right.inorder()
        return left + middle + right

    # ----------------------------------------------------------------
    # Question 2
    #
    # Complete the special member function `contains(x)` where `x` is
    # an integer. This function returns `True` if `x` is contained in
    # one of the intervals in the diet, and `False` otherwise.
    #
    # You are not allowed to use `.inorder()` to implement this function.
    #
    # Examples:
    #   >>> test_diet = ... # Diet given above
    #   >>> test_diet.contains(2)
    #   True
    #   >>> test_diet.contains(30)
    #   False
    #
    # Test with: python3 -m unittest tests.Diet.test_contains

    def contains(self, x: int):
        if x > self.hi and self.right is not None:
            return self.right.contains(x)
        if x < self.lo and self.left is not None:
            return self.left.contains(x)
        if x >= self.lo and x <= self.hi:
            return True
        return False

    # ----------------------------------------------------------------
    # Question 3
    #
    # Complete the member function `check_diet_invariant()` that
    # checks whether all the properties of a diet hold.
    #
    # In particular:
    #
    #  - Every pair of intervals in the diet must be separated.
    #
    #  - The diet must be a binary search tree, i.e.,
    #    the intervals in the left subtree
    #      $<~$ the interval at the root
    #      $<~$ the intervals in the right subtree.
    #
    #  - Every subtree of a diet should itself be a diet.
    #
    # The member function returns `False` if the invariant is
    # violated, and `True` otherwise.
    #
    # You are free to use recursion, `contains(), and `.inorder()` to
    # implement this.
    #
    # Do not worry about efficiency.
    #
    # Examples:
    #   >>> test_diet = ... # Diet given above
    #   >>> test_diet.check_diet_invariant()
    #   True
    #
    # Test with: python3 -m unittest tests.Diet.test_invariant

    def check_diet_invariant(self) -> bool:
        left_check, right_check = True, True
        if self.lo > self.hi:
            return False
        if self.left is not None:
            if self.left.hi + 1 >= self.lo:
                return False
            left_check = self.left.check_diet_invariant()
        if self.right is not None:
            if self.right.lo - 1 <= self.hi:
                return False
            right_check = self.right.check_diet_invariant()
        return left_check and right_check

    # ----------------------------------------------------------------
    # Question 4
    #
    # In a given diet, the largest interval is the rightmost
    # descendant of the root, and similarly the smallest interval is
    # the leftmost descendant of the root.
    #
    # You are given two member functions, `.unlink_largest()` and
    # `.unlink_smallest()` that, given a non-empty diet, returns a
    # pair of the largest/smallest interval and the rest of the diet.
    #
    #
    # For instance, suppose `test_diet` is the diet from earlier:
    #
    #                        (5, 10)
    #                        /     \
    #                       /       \
    #                    (2, 2)   (13, 14)
    #
    # Then, if we run the following, we observe:
    #
    # >>> (intv, remaining_diet) = test_diet.unlink_largest()
    # >>> intv
    # (13, 14)
    # >>> remaining_diet.inorder()
    # [2, 5, 6, 7, 8, 9, 10]
    # >>> (intv, remaining_diet) = test_diet.unlink_smallest()
    # >>> intv
    # (2, 2)
    # >>> remaining_diet.inorder()
    # [5, 6, 7, 8, 9, 10, 13, 14]
    #
    # Note that the original diet on which `.unlink_largest()` /
    # `.unlink_smallest()` is called is not altered.
    #
    # Instead, a new diet is created that is like the original diet
    # but without its largest/smallest interval.
    #
    # Using `.unlink_largest()` and `.unlink_smallest()`, write a
    # member function `.insert(x)` that inserts `x` into the diet and
    # that ensures that the diet invariant holds when it returns.
    #
    # Examples:
    #   >>> test_diet = ... # Diet given above
    #   >>> test_diet.contains(12)
    #   False
    #   >>> test_diet.insert(12)
    #   >>> test_diet.contains(12)
    #   True
    #   >>> test_diet.check_diet_invariant()
    #   True
    #
    # Test with: python3 -m unittest tests.Diet.test_insert

    def unlink_largest(self):
        """Return a diet like self, except without its largest interval"""
        if self.right is None:
            return ((self.lo, self.hi), self.left)
        else:
            (intv, rt) = self.right.unlink_largest()
            return (intv, DietNode(self.lo, self.hi, self.left, rt))

    def unlink_smallest(self):
        """Return a diet like self, except without its smallest interval"""
        if self.left is None:
            return ((self.lo, self.hi), self.right)
        else:
            (intv, lf) = self.left.unlink_smallest()
            return (intv, DietNode(self.lo, self.hi, lf, self.right))

    def insert(self, x):
        pass


# ====================================================================
# II. (Problem 3) Graphs

# Given a directed acyclic graph `G` (DAG) of `n` nodes labeled from
# `0` to `n - 1`, find all possible paths from node `0` to node `n - 1`
# and return them in any order. The graph `G` is encoded using an
# adjacency list and is guaranteed to be acyclic.
#
# Examples:
#   >>> all_paths(5, [[4, 3, 1], [3, 2, 4], [3], [4], []])
#   [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]]
#
# Test with: python3 -m unittest tests.AllPaths


def all_paths(n: int, G: List[List[int]]) -> List[List[int]]:
    paths = [[] for _ in range(n)]
    paths[0] = [[0]]
    seen = set([0])
    deque = [0]
    while deque:
        node = deque.pop()
        for neighbor in G[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                deque.append(neighbor)
            for path in paths[node]:
                paths[neighbor].append(path + [neighbor])
    return paths[-1]


# There is a group of `n` people labeled from `0` to `n - 1` where
# each person has a different amount of money and a different level of
# quietness.
#
# You are given an array richer where `richer[i] = (ai, bi)` indicates
# that `ai` has more money than `bi`, and an integer array `quiet`
# where `quiet[i]` is the quietness of the i-th person. All the given
# data in `richer` are logically correct (i.e., the data will not lead
# you to a situation where `x` is richer than `y` and `y` is richer
# than `x` at the same time).
#
# Return an integer array `answer` where `answer[x] = y` if `y` is the
# most quiet person (that is, the person `y` with the smallest value
# of `quiet[y]`) among all people who definitely have equal to or more
# money than the person `x`.
#
# Hint: construct a graph `G` s.t. there is an edge from `i` to `j` in
# `G` if `j` is richer than `i`. Then, write a (preferably memoized)
# function `quieter_at(i)` that returns the most quiet person that is
# reachable from `i` in `G`. Conclude.
#
# Examples:
#   >>> loud_and_rich([[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]], [3, 2, 5, 4, 6, 1, 7, 0])
#   [5, 5, 2, 5, 4, 5, 6, 7]
#
# Test with: python3 -m unittest tests.LoudAndRich


def quieter_at(i: int, G: List[List[int]], quiet: List[int]) -> int:
    if G[i] == []:
        return i
    else:
        deque = [i]
        seen = set([i])
        most_quiet = i
        while deque:
            node = deque.pop()
            if quiet[node] < quiet[most_quiet]:
                most_quiet = node
            for neighbor in G[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    deque.append(neighbor)
        return most_quiet


def loud_and_rich(richer: List[List[int]], quiet: List[int]) -> List[int]:
    n = len(quiet)
    G = [[] for _ in range(n)]
    for (i, j) in richer:
        G[j].append(i)
    return [quieter_at(i, G, quiet) for i in range(n)]


# ====================================================================
if __name__ == "__main__":
    _my_tests()
