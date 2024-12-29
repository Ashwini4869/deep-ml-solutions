import numpy as np


def accuracy_score(y_true, y_pred):
    total_preds = y_true.size
    correct_preds = 0
    for i in range(total_preds):
        if y_true[i] == y_pred[i]:
            correct_preds += 1

    return correct_preds / total_preds
