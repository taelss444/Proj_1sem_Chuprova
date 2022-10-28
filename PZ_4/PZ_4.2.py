# Ввод числа
N = input("Введите число: ")
# Обработка исключений
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("Неправильный ввод.")
        N = input("Введите число: ")
# Цикл
k = 0
while 3**k < N:
    k += 1
if 3**k == N:
    print("TRUE")
else:
    print("FALSE")
