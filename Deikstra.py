def deikstra(matrix, start, end):
    n = len(matrix)
    dist = [float('inf')] * n
    visit = [False] * n
    dist[start] = 0

    for i in range(n):
        min_cur = float('inf')
        current = 0
        for vertex in range(n):
            if dist[vertex] < min_cur and not visit[vertex]:
                min_cur = dist[vertex]
                current = vertex
        for neighbour in range(n):
            if matrix[current][neighbour] != 0 and not visit[neighbour]:
                new_dist = dist[current] + matrix[current][neighbour]
                if new_dist < dist[neighbour]:
                    dist[neighbour] = new_dist
        visit[current] = True
    return dist[end]

n = int(input("Введите размер матрицы: "))
print("Заполните матрицу")
matrix = [list(map(int, input().split())) for i in range(n)]
start = int(input("Введите начальную вершину: ")) - 1
end = int(input("Введите конечную вершину: ")) - 1

res = deikstra(matrix, start, end)
print(f"Длина пути из вершины {start + 1} в {end + 1}: {res}")
