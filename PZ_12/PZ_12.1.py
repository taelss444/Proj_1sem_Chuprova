# 1.Дана последовательность целых чисел. Поменять местами ее первую и
# последнюю трети.

import random

lst = [random.randint(-50, 50) for _ in range(int(input('Введите количество чисел : ')))]
print(f'Ваша последовательность : {lst}')
lst[0:len(lst)//3], lst[len(lst)//3*2:] = lst[len(lst)//3*2:], lst[0:len(lst)//3]
print(f'Измененная последовательность : {lst}')