import sys

sys.setrecursionlimit(10**6)


def catalan(n: int) -> int:
    """
    Naive recursive implementation of Catalan numbers.
    """
    if n < 1:
        return 1
    else:
        return sum(catalan(i) * catalan(n - i - 1) for i in range(n))


def catalan_td(n: int, cache: dict = None) -> int:
    """ """
    cache = {} if cache is None else cache
    if n not in cache:
        if n < 1:
            cache[n] = 1
        else:
            cache[n] = sum(catalan_td(i, cache) * catalan_td(n - i - 1, cache) for i in range(n))
    return cache[n]


def next_catalan(lst: list) -> int:
    """
    Given a list of Catalan numbers, return the next Catalan number.
    """
    n = len(lst)
    if n == 0:
        return 1
    return sum(lst[i] * lst[n - i - 1] for i in range(n))


def catalan_bu(n: int) -> int:
    """
    Bottom-up implementation of Catalan numbers.
    """
    catalans = []
    for _ in range(n + 1):
        catalans.append(next_catalan(catalans))
    return catalans[n]
