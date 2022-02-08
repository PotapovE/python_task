# 3. Вывести на экран числа от -N до N

def show (n):
    first_array = []
    if n < 0:
        n *= -1
    for i in range(-n, n + 1):
        first_array.append(i)
    return first_array
print(show(5))