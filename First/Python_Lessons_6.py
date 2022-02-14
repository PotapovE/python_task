# Кортеж
tuple = ("chek", 3, 5,)
# tuple[1] = 7 # Eror - кортеж неизменяемый тип данных
print(tuple)
print(list(tuple)) # Из кортежа в список

# Словарь
dict = {"apple": "red", "banana": "yelow", "limon": "yelow"}
print(dict)
for i in dict.keys(): # .keys - Выводит ключи словаря
    print(i)
for i in dict.values(): # .value - Выводит знвчения словаря
    print(i)
for i in dict.items(): # .items - Выводит словарЬ
    print(i)
print(dict["apple"]) # Вывод значения по ключу
dict["apple"] = "green" # Замена значения по ключу
print(dict["apple"])
del(dict["banana"]) # del() - Удаление элемента из словаря
print(dict)
dict["banana"] = "green"
print(dict)

if dict["banana"] == "yelow":
    print("Да")
else:
    print("Не очень!")