# Даны два списка А и В одинакового размера N.
# Сформировать новый список С того же размера,
# каждый элемент которого равен максимальному из элементов списков А и В.
from random import randint
N = input("Введите длину списков: ")
try:
    N = int(N)
    A = [randint(0, 11) for i in range(N)]
    B = [randint(0, 11) for i in range(N)]
    print("Список А:", A)
    print("Список В:", B)
    C = []
    for i in range(0, N):
        C.append(max(A[i], B[i]))
    print("Список С:", C)
except ValueError:
    print("Неверный ввод")
