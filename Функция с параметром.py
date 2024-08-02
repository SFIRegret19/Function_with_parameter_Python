def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([0] * m)
        for j in range(m):
            matrix[i][j] = value
    return matrix

print(get_matrix(1,2,5))
print(get_matrix(2,4,10))
print(get_matrix(4,4,20))