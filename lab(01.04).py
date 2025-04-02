def alg(matrix, start, end):
    height = len(matrix)
    width = len(matrix[0])
    start_i, start_j = start
    end_i, end_j = end

    matrix[start_i][start_j] = 1
    current = 1

    while matrix[end_i][end_j] == 0:
        flag = False
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == current:
                    for d_i, d_j in [(0,1),(1,0),(0,-1),(-1,0)]:
                        n_i = i + d_i
                        n_j = j + d_j
                        if matrix[n_i][n_j] == 0:
                            matrix[n_i][n_j] = current + 1
                            flag = True
        if not flag:
            break
        current += 1

    if matrix[end_i][end_j] > 0:
        return matrix[end_i][end_j] - 1
    else:
        return -1

n = int(input("Введите размер матрицы: "))
print("Заполните матрицу, где '-1' - это стена, а остальные элементы - '0': ")
nmatrix = [list(map(int, input().split())) for i in range(n)]
start = tuple(map(int, input("Введите координаты старта (i j): ").strip().split()))
end = tuple(map(int, input("Введите координаты финиша (i j): ").strip().split()))

matrix = [[-1] * (n + 2)]
for i in nmatrix:
    new_i = [-1] + i + [-1]
    matrix.append(new_i)
matrix.append([-1] * (n + 2))

res = alg(matrix, start, end)

if res > 0:
    print(f"Длина пути: {res}")
else:
    print("Путь не существует")