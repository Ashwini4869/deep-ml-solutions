import numpy as np


def batch_iterator(X, y=None, batch_size=64):
    batch_dataset = []
    num_data = X.shape[0]
    for i in np.arange(0, num_data, batch_size):
        begin, end = i, min(i + batch_size, num_data)
        if y is not None:
            batch_dataset.append([X[begin:end], y[begin:end]])
        else:
            batch_dataset.append([X[begin:end]])

    return batch_dataset
