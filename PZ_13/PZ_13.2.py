#В матрице элементы второго столбца возвести в квадрат.
matrix = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
matrix_length = len(matrix)
for i in range(matrix_length):
    print(matrix[i][1]**2)
