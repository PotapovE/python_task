# Множества
numbers = {1, 5, 7, 11, 48, 54, 68}
empty_set = set() # set() - Создать пустое множество
print(numbers)
print(type(empty_set))
full_numbers = [1, 1, 5, 7, 90, 7, 81, 3, 11]
sort_set = set(full_numbers) # Сортировка списка множеством
print(sort_set)

# Меотды работы с множеством
for i in sort_set: # Вывод элементов множества
    print(i)
print(3 in sort_set) # Поиск элемента во множестве (True, False)
sort_set.add(55) # .add() - Добавить элемент множества
sort_set.discard(99) # .discard() - Удаляет элемент из множества
sort_set.remove(3) # .remove() - Удаляет присутствующий элемент из множества 
sort_set.pop() # .pop() - Удаляет первый элемент
# sort_set.clear() # .clear() - Удаляет все элементы
print(sort_set) 
res_set = numbers.union(sort_set) # .union() - Объединение множеств
res_set = numbers | sort_set # | - Вариант объединения множеств
print(res_set)
res_set = numbers.intersection(sort_set) # .intersection() - Пересечение множеств
res_set = numbers & sort_set # & - Вариант записи пересечения множеств
print(res_set)
res_set = numbers - sort_set # "-" - Разница множеств
print(res_set)
res_set = sort_set.copy() # .copy() - Копирование множества
print(res_set)