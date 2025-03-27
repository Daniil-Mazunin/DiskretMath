def kruskal(matrix):
    sum = 0
    edge = []
    components = [i for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != 0:
                edge.append((matrix[i][j], i, j))
    edge.sort()
    ostov = []
    for weight, i, j in edge:
        if components[i] != components[j]:
            ostov.append((i + 1, j + 1))
            sum += weight
            old_components = components[j]
            for k in range(n):
                if components[k] == old_components:
                    components[k] = components[i]
    return ostov, sum

n = int(input("Введите размер матрицы смежности: "))
print("Введите элементы матрицы смежности: ")
matrix = [list(map(int, input().split())) for i in range(n)]
edge, sum = kruskal(matrix)
print(f"Общий вес: {sum}, Ребра: {edge}")
