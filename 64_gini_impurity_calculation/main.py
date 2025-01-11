import numpy as np


def gini_impurity(y):
    """
    Calculate Gini Impurity for a list of class labels.

    :param y: List of class labels
    :return: Gini Impurity rounded to three decimal places
    """
    labels = set(y)
    n = len(y)

    gini_impurity = 0

    for item in labels:
        gini_impurity += (y.count(item) / n) ** 2

    return round(1 - gini_impurity, 3)
