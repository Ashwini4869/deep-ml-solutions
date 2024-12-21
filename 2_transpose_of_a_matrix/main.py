def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    # Define a matrix by reversing the order of matrix a
    b = [[0 for i in range(len(a))] for j in range(len(a[0]))]

    # Perform the transpose
    for i in range(len(a)):
        for j in range(len(a[i])):
            b[j][i] = a[i][j]
    return b
