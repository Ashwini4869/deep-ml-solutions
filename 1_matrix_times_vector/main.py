def matrix_dot_vector(
    a: list[list[int | float]], b: list[int | float]
) -> list[int | float]:
    # Create a list of expected size filled with zeros
    c = [0] * len(b)

    # Check if the dimensions match
    if len(a[0]) == len(b):
        for i in range(len(b)):
            for j in range(len(a[i])):
                c[i] += a[i][j] * b[j]

    # Return -1 if dimensions do not match
    else:
        c = -1
    return c
