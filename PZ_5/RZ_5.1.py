n = input("Введите первое число: ")
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильный ввод.")
        n = int(input("Введите первое число: "))
m = input("Введите последнее число: ")
while type(m) != int:
    try:
        m = int(m)
    except ValueError:
        print("Неправильный ввод.")
        m = int(input("Введите первое число: "))

def summa_chisel(n, m):
    s = 0
    for i in range(n, m+1):
        s = i + s
    print("Сумма чисел от", n, "до", m, "равна", s)


summa_chisel(n, m)