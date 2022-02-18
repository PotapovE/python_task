# Лямбда функция
def area (a, b):
    return a * b
print(area(5,4))
print((lambda a, b: a * b) (3, 4))
# Вывести большее число
print((lambda x, y: x if x > y else y) (23, 15))
# Написать lambda-функцию, принимающую 1 аргумент — сторону квадрата, и возвращающую периметр квадрата.
print((lambda x: x*4) (4))