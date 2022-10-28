K = input("Введите целое положительное число: ")
while type(K) != int:
    try:
        K = int(K)
    except ValueError:
        print("Неправильный ввод.")
        K = int(input("Введите целое положительное число: "))


def DigitCountSum(K):
    C = 0
    S = 0
    while K > 0:
        S += K % 10
        K //= 10
        C = C + 1
    print("Количество цифр целого числа:",C,"\n","Сумма цифр целого положительного числа:", S)


DigitCountSum(K)