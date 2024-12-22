def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    # Initialize empty list to store means
    means = []
    if mode == "row":
        for i in range(len(matrix)):
            means.append(sum(matrix[i]) / len(matrix[i]))

    elif mode == "column":
        for i in range(len(matrix)):
            sum_col = 0
            for j in range(len(matrix[i])):
                sum_col += matrix[j][i]
            means.append(sum_col / len(matrix[i]))
    return means
