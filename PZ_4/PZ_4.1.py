a, b = input("Введите первое число: "), input("Введите второе число: ")
# Обработка исключений
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильный ввод.")
        a = input("Введите первое число: ")
# Обработка исключений
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильный ввод.")
        b = input("Введите второе число: ")
# Цикл while
k = 0
while a <= b:
    print(a)
    a += 1
    k += 1
print("Количество чисел:", k)
