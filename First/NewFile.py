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
