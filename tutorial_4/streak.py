import random
from typing import List


def is_there_a_streak(sequence: List[int], k: int) -> bool:
    """Return True if there is a streak of k or more 1s in sequence."""
    streak = 0
    for flip in sequence:
        streak += flip
        if streak >= k:
            return True
        if flip == 0:
            streak = 0
    return False


def experiment1(N: int, k: int):
    sequence = random.choices([0, 1], k=N)
    return is_there_a_streak(sequence, k)


def experiment(N: int, k: int, trials: int = 100_000):
    return sum(experiment1(N, k) for _ in range(trials)) / trials
