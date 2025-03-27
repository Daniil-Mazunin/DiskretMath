def prima(matrix):
    sum = 0
    visit = [1]
    while (len(visit) != len(matrix)):
        min_edge = 0
        index = 0
        for i in visit:
            k = i - 1
            for j in range(len(matrix)):
                if (matrix[k][j] < min_edge or min_edge == 0) and (not j + 1 in visit) and (matrix[k][j] != 0):
                    min_edge = matrix[k][j]
                    index = j + 1
        visit.append(index)
        sum += min_edge
    return sum

n = int(input("Введите размер матрицы смежности: "))
print("Введите элементы матрицы смежности: ")
matrix = [list(map(int, input().split())) for i in range(n)]
sum = prima(matrix)
print("Общий вес: ", sum)

