#Дана строка "апельсины 45 991 63 100 12 яблоки 13 47 26 0 16",
# отражающая продажи продукции по дням в кг. Преобразовать информацию
#из строки в словари, с использованием функции найти среднее
#значение продаж по каждому виду продукции, результаты вывести на экран.
fruits = {}
products = "апельсины 45 991 63 100 12 яблоки 13 47 26 0 16"
products = products.split()
fruits['апельсины'] = []
for i in products[1:6]:
    fruits['апельсины'].append(int(i))
fruits['яблоки'] = []
for k in products[7:12]:
    fruits['яблоки'].append(int(k))
print(fruits)


def sale():
    average_value = dict()
    for key in fruits:
        average_value[key] = sum(fruits[key]) / len(fruits[key])
    print("Среднее значение продаж:", str(average_value))


sale()
