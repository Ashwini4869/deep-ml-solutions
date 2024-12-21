import math


def softmax(scores: list[float]) -> list[float]:
    # Your code here
    exponential_scores_sum = sum([math.exp(scores[i]) for i in range(len(scores))])
    probabilities = [
        round((math.exp(scores[i])) / exponential_scores_sum, 4)
        for i in range(len(scores))
    ]
    return probabilities
