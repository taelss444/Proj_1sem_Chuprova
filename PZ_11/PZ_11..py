import random

f1 = open('file1.txt', 'w+')
f2 = open('file2.txt', 'w+')

for i in range(-6, 6):
    f1.write(f'{str(random.randrange(-6, 6))}\n')
    f2.write(f'{str(random.randrange(-7, 7))}\n')
f1.close()
f2.close()
f1 = open('file1.txt')
f2 = open('file2.txt')

read = f1.readlines()
read2 = f2.readlines()
n = []
for i in read:
    n.append(int(i.replace('\n', '')))

m = []
for i in read2:
    m.append(int(i.replace('\n', '')))
print(n, '\n', m)

all = n + m
poryadok = sorted(all)
lenth = len(all)
all1 = [i for i in all]
res = min(filter(lambda x: x%2==0, all1))

all2 = [i for i in all]
res2 = max(filter(lambda x: x%5==0, all2))
f3 = open("file3.txt", 'w+')
f3.write(f'''Элементы первого и второго файлов: {all} 
Элементы после сортировки: {poryadok}
Количество элементов: {lenth}
Mинимальный элемент кратный 2: {int(res)}
Максимальный элемент кратный 5: {int(res2)}''')

f3.close()
f3 = open('file3.txt')
print(f3.read())