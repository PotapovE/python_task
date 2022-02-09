# 3. Вывести на экран числа от -N до N
import math

n = abs(int(input()))
data = [i for i in range(-n, n+1)]
print (data)