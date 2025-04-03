def fordBelman(matrix, start):
    inf = float('inf')
    dist = [inf]*n
    dist[start] = 0
    for k in range(1, n):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] != 0 and dist[i] != inf and dist[i] + matrix[i][j] < dist[j]:
                    dist[j] = dist[i] + matrix[i][j]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0 and dist[i] != inf and dist[i] + matrix[i][j] < dist[j]:
                print("Отрицательный цикл")
                return
    return dist

n = int(input("Введите размер матрицы: "))
print("Заполните матрицу")
matrix = [list(map(float, input().split())) for i in range(n)]
start = int(input("Введите начальную вершину: ")) - 1

res = fordBelman(matrix, start)
print(res)