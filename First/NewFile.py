# Найти расстояние между двумя точками пространства
import math

A = (0, 4)
B = (0, 6)
def answer (point_a, point_b):
    return math.sqrt(math.pow(point_b[0]-point_a[0], 2) + math.pow(point_b[1]-point_a[1], 2))
print(answer(A, B))