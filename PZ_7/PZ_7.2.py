#Даны строки S, S1 и S2. Заменить в строке S последнее
#вхождение строки S1 на строку S2.
S = input("Введите первую строку: ")
S1 = input("Введите вторую строку: ")
S2 = input("Введите третью строку: ")
p = S.rfind(S1)
print(S + S.replace(S[:p], S2))
