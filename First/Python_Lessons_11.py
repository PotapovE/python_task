# Множества
numbers = {1, 5, 7, 11}
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
sort_set.add(33) # .add() - Добавить элемент множества
sort_set.discard(99) # .discard() - Удаляет элемент из множества
sort_set.remove(33) # .remove() - Удаляет присутствующий элемент из множества 
print(sort_set) 
