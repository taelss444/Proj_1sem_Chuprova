# 2.Составить генератор (yield), который выводит из строки только цифры.

def digiter(st: str):
    yield "".join(c for c in st if c.isdigit())


print(f'Ваши цифры : {next(digiter(input("Введите строку : ")))}')