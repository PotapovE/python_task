# Работа с файлами
data = open("text.txt", "w") # - r - чтение, w - перезапись, a - дописать
data.write("Hello World!")
data.close()

bufer = open("text.txt", "r")
print(bufer.read())
bufer.close()

with open("text.txt", "a") as res: # - конструкция автоматического закрытия файла
    res.write("\nOk, let's go!")

# Исключения
try:
    a = int(input("a: "))
    b = int(input("b: "))
    print(a/b)
except ZeroDivisionError:
    print("На ноль делить нельзя!")