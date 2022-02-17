# Регулярные выражения
import re

text = """С другой стороны сложившаяся структура организации представляет собой интересный эксперимент проверки 
существующих финансовых и административных условий! Практический опыт показывает, что курс на социально-ориентированный 
национальный проект играет важную роль в формировании позиций, занимаемых участниками в отношении поставленных задач? 
С другой стороны выбранный нами инновационный путь способствует повышению актуальности позиций, занимаемых участниками 
в отношении поставленных задач."""
result = re.match("С", text) # .match() - Определяет, еслть ли искомое выражение в начале строки
print(result)
result = re.search("и", text) # .search() - поиск первого шаблона во всем тексте
print(result) # result[i] - Выводит искомый шаблон
result = re.findall("ой", text) # .findall() - Создаёт список со всеми найденными шаблонами в тексте
print(result)
result = re.split("\n", text) # .split() - Создает список по ключу (maxsplit= - количество разбивок)
print(result)