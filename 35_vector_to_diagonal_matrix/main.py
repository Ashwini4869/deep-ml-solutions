import numpy as np


def make_diagonal(x):
    size = x.size
    diagonal_matrix = np.zeros(shape=(size, size))
    for i in range(diagonal_matrix.shape[0]):
        for j in range(diagonal_matrix.shape[1]):
            if i == j:
                diagonal_matrix[i][j] = x[i]
    return diagonal_matrix.tolist()
