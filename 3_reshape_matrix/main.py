import numpy as np


def reshape_matrix(
    a: list[list[int | float]], new_shape: tuple[int, int]
) -> list[list[int | float]]:
    a_np = np.asarray(a)
    reshaped_matrix = (np.reshape(a_np, new_shape)).tolist()
    return reshaped_matrix
