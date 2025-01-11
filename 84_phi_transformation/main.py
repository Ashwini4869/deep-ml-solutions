import numpy as np


def phi_transform(data: list[float], degree: int) -> list[list[float]]:
    """
    Perform a Phi Transformation to map input features into a higher-dimensional space by generating polynomial features.

    Args:
            data (list[float]): A list of numerical values to transform.
            degree (int): The degree of the polynomial expansion.

    """
    if degree < 1 or not data:
        return []

    phi_transform = []
    degree_list = range(degree + 1)
    for item in data:
        item_np = np.array(item)
        item_transform = np.power(item_np, degree_list).tolist()
        phi_transform.append(item_transform)

    return phi_transform
