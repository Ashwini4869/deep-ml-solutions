import math


def single_neuron_model(
    features: list[list[float]], labels: list[int], weights: list[float], bias: float
) -> (list[float], float):
    n = len(features)
    z = [0 for i in range(n)]
    probabilities = z
    mse = 0
    for i in range(n):
        z[i] = sum(x * y for x, y in zip(features[i], weights)) + bias

    for i in range(n):
        probabilities[i] = round(1 / (1 + math.exp(-z[i])), 4)

    for i in range(n):
        mse += (probabilities[i] - labels[i]) ** 2
    mse = round(mse / n, 4)
    return probabilities, mse
