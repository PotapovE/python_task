# 14. Подсчитать сумму цифр в вещественном числе.
print(sum([int(i) for i in str(abs(float(input('Введите число через точку: ')))).replace('.','')]))