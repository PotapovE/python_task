# Регулярные выражения
import re

text = "485734590-543   54%+nugrkjehg4tg3rerg4+g4  r4etet4534erg"
result = re.search(r"n..r", text) # r"i...j" - Шаблон для поиска с известными первым и последним символом
result = re.search(r"\d\d\d\d\d\d\d\d", text) # \d - Вывод цифр по шаблону (\+, \* - продолжает шаблон до другого символа)
result = re.search(r"\D", text) # \D - Вывод символа кроме цифры по шаблону
result = re.search(r"\s", text) # \s - Вывод (\S кроме) пробела по шаблону
result = re.search(r"\w", text) # \w - Вывод (\W кроме) буквы, цифры, "_" по шаблону
result = re.search(r"\b73", text) # \b - Вывод (\B середина) начала или конца слова по шаблону
result = re.search(r"[^3-7]", text) # [] - Диапазон поиска (^) - кроме
result = re.search(r"3|%", text) # | - Первый вывод одного из
# Квантификатор
# {3}, {1,3}, {2,} {,2}