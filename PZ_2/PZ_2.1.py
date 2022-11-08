#С начала суток прошло N секунд (N – целое).
# Найти количество полных часов, прошедших с начала суток.
n = input('Введите секунды: ')
while type(n) != int:    #Обработка исключений
    try:
        n = int(n)
    except ValueError:
        print("Неправильный ввод.")
        n = input("Введите секунды: ")
print('Прошло полных часов:', int(n/60/60))