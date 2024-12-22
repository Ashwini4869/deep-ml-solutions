import numpy as np


def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    # Standardized data
    mean_data = np.mean(data, axis=0)
    mean_std = np.std(data, axis=0)
    standardized_data = np.round(((data - mean_data) / mean_std), 4)

    # Normalized data
    min_data = np.min(data, axis=0)
    max_data = np.max(data, axis=0)
    normalized_data = np.round(((data - min_data) / (max_data - min_data)), 4)

    return standardized_data, normalized_data
