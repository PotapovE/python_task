# 1. По двум заданным числам проверить является ли одно квадратом второго
x = 4
y = 2
print(x**2 == y or y**2 == x)

# 2. Найти максимальное из пяти чисел
numbers = [3, 6, 4, 9, 4]
print (max(numbers))

# 3. Вывести на экран числа от -N до N
import math

n = abs(int(input()))
data = [i for i in range(-n, n+1)]
print (data)

# 4. Показать первую цифру дробной части числа
x = 10.345
x = ((x * 10) % 10)
print(int(x))

# 5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
a = 10
print((not a % 5 and (not a % 10 or not a % 15) and not a % 30 == 0))

# 6. Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
a = 6
weak_day = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
print(weak_day[a-1])
if a < 6:
    print("тяжелые будни")
else:
    print("Ура, пляшем!")

# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
x = True
y = False
z = True
a = (not (x or y or z))
b = (not x and not y and not z)
print(a == b)

# 8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У
def answer(x, y):
    if x > 0 and y > 0 : return '1'
    elif x < 0 and y > 0 : return '2'
    elif x < 0 and y < 0 : return '3'
    elif x > 0 and y < 0 : return '4'
    if x == 0 and y == 0 : return '1, 2, 3, 4'
    elif x == 0 and y > 0 : return '1, 2'
    elif x == 0 and y < 0 : return '3, 4'
    elif x > 0 and y == 0 : return '1, 4'
    elif x < 0 and y == 0 : return '2, 3'   
print(answer(-3, 0))
