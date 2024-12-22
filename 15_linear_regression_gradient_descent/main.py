import numpy as np


def linear_regression_gradient_descent(
    X: np.ndarray, y: np.ndarray, alpha: float, iterations: int
) -> np.ndarray:
    # Your code here, make sure to round
    m, n = X.shape
    theta = np.zeros((n, 1))
    for _ in range(iterations):
        # Calculate predictions
        y_pred = X @ theta
        # Calculate errors
        errors = y_pred - y.reshape(-1, 1)
        # Calculate update value
        update = X.T @ errors
        # Update theta
        theta -= (alpha / m) * update
    # Update to four decimal places
    theta = np.round(theta, 4)
    return theta
