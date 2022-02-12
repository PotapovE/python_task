# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У

def answer(x, y):
    if x > 0 and y > 0 : return '1'
    elif x < 0 and y > 0 : return '2'
    elif x < 0 and y < 0 : return '3'
    elif x > 0 and y < 0 : return '4'
    if x == 0 and y == 0 : return '1, 2, 3, 4'
    elif x == 0 and y > 0 : return '1, 2'
    elif x == 0 and y < 0 : return '3, 4'
    elif x > 0 and y == 0 : return '1, 4'
    elif x < 0 and y == 0 : return '2, 3'
    
print(answer(-3, 0))