# Генератор списка
s = [i for i in range(21) if i % 5 == 0]
print(s)
# Пример с полным ветвлением
s = [i ** 2 if i > 0 else i ** 3 for i in range(-10, 11) if i % 2 != 0]
print(s)