# Регулярные выражения
import re

text = "485734590-543   54%+nugrkjehg4tg3rerg4+g4  r4etet4534erg"
result = re.search(r"n..r", text) # r"i...j" - Шаблон для поиска с известными первым и последним символом
print(result)
result = re.search(r"\d\d\d\d\d\d\d\d", text) # \d - Вывод цифр по шаблону
print(result)
result = re.search(r"\D", text) # \D - Вывод символа кроме цифры шаблону
print(result)
result = re.search(r"\s", text) # \s - Вывод (\S кроме) пробела по шаблону
print(result)