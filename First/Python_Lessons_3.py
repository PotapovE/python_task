# Функции
def hello ():
    print("Привет, Мир!")

hello()

# Функция сложения
x = int(input("Введите число - "))
y = int(input("Введите число - "))

def sum (a, b):
    return a + b

z = sum (x, y)
print (z)

# Необязательный аргумент
def sum (a, b=3):
    return a + b

print(sum(1))

# Глобальная переменная

a = 33
def f ():
    global a
    a *= 2
    print(a)
    
f()
print(a)