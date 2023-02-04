#В матрице найти сумму элементов второй половины матрицы.
matrix = [[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]]
matrix_length = len(matrix)


def sumColumn(matrix, column, column2):
    part = 0
    part2 = 0
    for row in range(matrix_length):
        part += matrix[row][column]
        part2 += matrix[row][column2]
    total = part + part2
    return total


column = -1
column2 = 2
print(sumColumn(matrix, column, column2))
