def zigzag_traversal(matrix):
    if not matrix:
        return []

    result = []
    rows, cols = len(matrix), len(matrix[0])

    for diag_sum in range(rows + cols - 1):
        if diag_sum % 2 == 0:
            for row in range(min(diag_sum, cols - 1), max(0, diag_sum - rows + 1) - 1, -1):
                result.append(matrix[diag_sum - row][row])
        else:
            for col in range(min(diag_sum, rows - 1), max(0, diag_sum - cols + 1) - 1, -1):
                result.append(matrix[col][diag_sum - col])

    return result
