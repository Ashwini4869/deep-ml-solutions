import numpy as np


def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
    B = np.asarray(B)
    C = np.asarray(C)
    C_inv = np.linalg.inv(C)
    P = np.dot(C_inv, B)
    return P.tolist()
