import numpy as np


def to_categorical(x, n_col=None):
    if n_col is None:
        n_col = len(np.unique(x))
    one_hot = []
    for item in x:
        temp_list = [0] * n_col
        temp_list[item] = 1
        one_hot.append(temp_list)

    return one_hot
