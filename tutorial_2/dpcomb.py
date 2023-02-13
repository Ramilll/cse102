from functools import lru_cache
from typing import Dict, List, Tuple


@lru_cache(maxsize=None)
def binom(n: int, k: int):
    """
    Return the binomial coefficient n choose k.
    """
    if k == 0 or k == n:
        return 1
    return binom(n - 1, k - 1) + binom(n - 1, k)


def binom_td(n: int, k: int, cache: dict = None) -> int:
    """
    Implementation of binom using storing intermediate results in a cache.
    """
    cache = {} if cache is None else cache
    if (n, k) in cache:
        return cache[n, k]
    if k == 0 or k == n:
        cache[(n, k)] = 1
        return 1
    cache[n, k] = binom_td(n - 1, k - 1, cache) + binom_td(n - 1, k, cache)
    return cache[(n, k)]


def binom_dp(n: int, k: int) -> int:
    """
    Implementation of binom using dynamic programming.
    """
    binom = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                binom[i][j] = 1
            else:
                binom[i][j] = binom[i - 1][j - 1] + binom[i - 1][j]
    return binom[n][k]


def parts_td(n, k=None, cache=None):
    cache = {} if cache is None else cache
    if k is None:
        return sum(parts_td(n, k, cache) for k in range(1, n + 1))
    if (n, k) in cache:
        return cache[n, k]
    if k > n:
        return 0
    if k == 1:
        return 1
    cache[n, k] = parts_td(n - 1, k - 1, cache) + parts_td(n - k, k, cache)
    return cache[n, k]


def parts_bu(n):
    cache = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        cache[i][1] = 1
    for i in range(2, n + 1):
        for j in range(2, i + 1):
            cache[i][j] = cache[i - 1][j - 1] + cache[i - j][j]
    return sum(cache[n][k] for k in range(1, n + 1))
