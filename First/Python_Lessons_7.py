# Работа со строками
print("""All 
day,
all
night""")
print("Hello\t'Hello'\n\"Hello\"")
text = "hello"
text1 = "World!"
print(text + " " + text1)
print(text * 5)
print(text[0])
print(text[0:2])
print(text[-1])
print(text.upper()) # .upper() - Заглавные буквы
print(text.lower()) # .lower() - Прописные буквы
print(text.capitalize()) # .capitalize() - Делает первую букву заглавной

# Конвертация строк в список
write = "Хочу еще этих булок"
result = write.split(" ") # .split(" ") - разбивает элементы строки в список по аргументу
print(result)
write_result = " ".join(result) # " ".join(list[]) - Складывает элементы списка в строку через аргумент " "
print(write_result)