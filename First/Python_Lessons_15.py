# Функция map
with open ("test.txt", "r") as text: # открывает документ
    value = int(text.readline()) # первая строка в файле = количеству строк
    for i in range(value): 
        a, b = map(int, text.readline().split()) # конвертация текста в числа
        print(a + b)