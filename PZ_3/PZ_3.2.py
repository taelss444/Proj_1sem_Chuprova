#Даны координаты поля шахматной доски x, y (целые числа в диапазоне 1-8).
# Учитывая, что левое нижнее поле доски (1,1) является черным,
# проверить истинность высказывания: «Данное поле является белым».
x, y = input("Введите координату x (от 1 до 8): "), input("Введите координату y (от 1 до 8): ")    #Ввод координат

while type(x) != int:    #Обработка исключений
    try:
        x = int(x)
    except ValueError:
        print("Неправильный ввод.")
        x = input("Введите координату x (от 1 до 8): ")

while type(y) != int:    #Обработка исключений
    try:
        y = int(y)
    except ValueError:
        print("Неправильный ввод.")
        y = input("Введите координату y (от 1 до 8): ")

if x % y == 1:
    print("Данное поле является белым")
else:
    print("Данное поле является черным")





