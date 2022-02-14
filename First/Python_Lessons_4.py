# Цикл For
name = "Hello, World!"
for i in name:
    print(i)

# Функция Range
name = "Hello, World!"
for i in range(1, 11): # 10 times
    print(i, name)

# Цикл While
i = 1
while i <= 10:
    print(i)
    i += 1

# Принудительный выход из цикла Break
i = 1
while i <= 10:
    print(i)
    i += 1
    break

# Продолжение выполнения цикла continue
i = 1
while i <= 10:
    if i != 3:
        print(i)
    i += 1
    continue