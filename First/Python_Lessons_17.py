# Генератор списка
from re import S


s = [i for i in range(21) if i % 5 == 0]
print(s)
# Пример с полным ветвлением
s = [i ** 2 if i > 0 else i ** 3 for i in range(-10, 11) if i % 2 != 0]
print(s)
# Генератор множества
l = [45, -45, 45, 55, -55, -55]
s = {i for i in l}
print(s)