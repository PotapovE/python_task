# Функция map
with open ("test.txt", "r") as text: # открывает документ
    value = int(text.readline()) # первая строка в файле = количеству строк
    for i in range(value): 
        a, b = map(int, text.readline().split()) # конвертация текста в числа
        print(a + b)
# Примеры
def func (a, b):
    return a * b
a = map(func, [3, 6, 7], [3, 4, 0])
print(list(a))
# Пример с лямбдой
a = map(lambda a, b: a * b, [3, 9], [5, 8])
print(list(a))

# Функция filter
def func (a):
    return a % 2 != 0
a = filter(func, [3, 6, 7])
print(list(a))

# Функция reduce
from functools import reduce

print(reduce(lambda x, y: x * y, [1, 3, 4, 5]))