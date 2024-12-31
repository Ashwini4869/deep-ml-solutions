import numpy as np


def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
    mse_loss = np.mean((y_true - X @ w) ** 2)
    penalty = alpha * np.sum(w**2)
    ridge_loss = mse_loss + penalty
    return ridge_loss
