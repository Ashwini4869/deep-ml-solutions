import numpy as np


def log_softmax(scores: list) -> np.ndarray:
    scores = np.array(scores)
    log_softmax = []
    max_score = max(scores)
    for score in scores:
        log_softmax_score = (
            score - max_score - np.log(np.sum(np.exp(scores - max_score)))
        )
        log_softmax.append(log_softmax_score)
    return np.round(np.asarray(log_softmax), 4).tolist()
