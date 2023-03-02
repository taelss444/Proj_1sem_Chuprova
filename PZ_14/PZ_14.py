import re

stations = open('Dostoevsky.txt','r', encoding='utf-8')
string_test = stations.read()
stations.close()
romans = list(set(re.findall(r'(Идиот|Преступление и наказание|Униженные и оскорблённые|Братья Карамазовы|Бедные люди|Двойник|Записки из мертвого дома|Записки из подполья|Зимние заметки о летних впечатлениях|Игрок|Бесы|Дневник писателя|Подросток|Кроткая)',string_test)))
print(f"Ваш файл: {string_test}")
print("Произведения Достоевского: ", romans)
print(f'Количество: {len(romans)}')
