# Списки
spisok = []
numbers = [2, 5, 7]
print(numbers)
feat = [3, 5.6, 'Hi']
print(feat)
feat[2] = "ok"
multi = [4, 6.7, 'chek', feat] 
print(multi)

# Вывод элементов списка
names = ["Dog", "Cat", "Caw"]
print(names[1]) # Индекс
print(names[-1]) # С конца списка

for name in names:
    print(name)

# Методы для работы со списками
names.append("pig") # .append - добавить элемент в конец списка
print(names)
names.pop() # .pop - удаляет последний лемент из списка
print(names)
i = names.index("Cat") # .index - Показывает индекс искомого элемента в списке
print(i)
print(len(names)) # len - Показывает количесво элементов в списке
values = [3, 10, 1, -5, 13]
values.sort(reverse=True) # .sort - Сортирует список (reverse = True - Обратная сортировка)
print(values)