import random
from typing import List

import matplotlib.pyplot as plt


def plot(ns):
    N = sum(ns)
    ns = [float(x) / N for x in ns]
    plt.bar(range(len(ns)), height=ns)
    plt.xticks(range(len(ns)), [str(i + 1) for i in range(len(ns))])
    plt.ylabel("Probability")
    plt.title("Biased die sampling")
    plt.show()


def roll(probabilities_of_side: list) -> int:
    """Simulated a roll of a die with the given probabilities."""
    r = random.random()
    cumulative_probability = 0
    for idx, prob in enumerate(probabilities_of_side):
        cumulative_probability += prob
        if r < cumulative_probability:
            return idx + 1


def rolls(probabilities_of_side: list, num_rolls: int) -> list:
    """Simulated a roll of a die with the given probabilities."""
    results = [roll(probabilities_of_side) for _ in range(num_rolls)]
    k = len(probabilities_of_side)
    summary_results = [0] * k
    for result in results:
        summary_results[result - 1] += 1
    return summary_results
