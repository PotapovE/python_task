# Регулярные выражения
import re

text = "485734590-543   54%+nugrkjehg4tg3rerg4+g4  r4etet4534erg"
result = re.search(r"n..r", text) # r"i...j" - Шаблон для поиска с известными первым и последним символом
print(result)