from typing import List


def win_probability(die1: List[int], die2: List[int]) -> float:
    winning_result = 0
    for d1 in die1:
        for d2 in die2:
            if d1 > d2:
                winning_result += 1
    return winning_result / (len(die1) * len(die2))


def beats(die1: List[int], die2: List[int]):
    return win_probability(die1, die2) > 0.5
