# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
n = int(input("Введите N: "))
s = [1]
res = 1
for i in range(1, n):
    res *= -3
    s.append(res)
print(s)