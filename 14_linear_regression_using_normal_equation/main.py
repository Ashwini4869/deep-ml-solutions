import numpy as np


def linear_regression_normal_equation(
    X: list[list[float]], y: list[float]
) -> list[float]:
    # Convert both to numpy arrays
    X_np = np.asarray(X)
    y_np = np.asarray(y)

    # Calculate theta using the normal equation
    X_np_T = np.transpose(X_np)

    X_np_T_X_inverse = np.linalg.inv(np.dot(X_np_T, X_np))

    theta = np.dot(np.dot(X_np_T_X_inverse, X_np_T), y_np)

    # Round off the values
    theta = np.round(theta, 4)

    return theta
