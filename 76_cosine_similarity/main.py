import numpy as np


def cosine_similarity(v1, v2):
    v1 = v1.flatten()
    v2 = v2.flatten()
    numerator = np.dot(v1, v2)
    denum_a = np.sqrt(np.sum(v1**2))
    denum_b = np.sqrt(np.sum(v2**2))
    return round(numerator / (denum_a * denum_b), 3)
