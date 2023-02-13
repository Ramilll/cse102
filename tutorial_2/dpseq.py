from copy import copy
from typing import List


def next_seq(alphas: List[int], us: List[int]) -> int:
    """
    Given a list of alphas and a list of us, return the next sequence number.
    """
    assert len(alphas) == len(us)
    return sum(alpha * u for alpha, u in zip(alphas, us))


def u(alphas: List[int], us: List[int], n: int) -> int:
    """
    Need to compute u_n given alphas and us.
    """
    assert len(alphas) == len(us)
    k = len(alphas)
    new_us = copy(us)
    while len(new_us) <= n:
        new_us.append(next_seq(alphas, new_us[-k:]))
    return new_us[n]
