# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

from operator import truediv
x = True
y = False
z = True
a = (not (x or y or z))
b = (not x and not y and not z)
print(a == b)