import random


def is_first_player_winner(t1: int, t2: int, t3: int) -> bool:
    return True if t1 == 1 and t2 == 1 and t3 == 0 else False


def is_second_player_winner(t1: int, t2: int, t3: int) -> bool:
    return True if t1 == 0 and t2 == 1 and t3 == 1 else False


def experiment1() -> bool:
    """True if 110 appears first in a sequence, false if 011 appears first."""
    t1, t2, t3 = random.choices([0, 1], k=3)
    while True:
        if is_first_player_winner(t1, t2, t3):
            return True
        if is_second_player_winner(t1, t2, t3):
            return False
        t1, t2, t3 = t2, t3, random.choice([0, 1])


def experiment(num_trials: int = 100_000) -> float:
    return sum(experiment1() for _ in range(num_trials)) / num_trials
