def floyd(matrix, n):
    inf = float('inf')
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] != inf and matrix[k][j] != inf:
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    return matrix

n = int(input("Введите размер матрицы: "))
print("Заполните матрицу")
matrix = [list(map(float, input().split())) for i in range(n)]

floyd(matrix, n)
print(matrix)