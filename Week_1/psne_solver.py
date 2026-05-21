import numpy as np
def solve_psne(p1_matrix, p2_matrix):
    n = len(p1_matrix)
    m = len(p1_matrix[0])
    row = []
    col = []

    for i in range(n):
        col.append((i ,int(np.argmax(p2_matrix[i]))))
    for i in range(m):
        row.append((int(np.argmax([p1_matrix[j][i] for j in range(n)])), i))
    psne = [cell for cell in row if cell in col]
    return psne

