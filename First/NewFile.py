# Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

def answer(number):
    if number == 1:
        return 'x >= 0, y >= 0'
    elif number == 2:
        return "x <= 0, y >= 0"
    elif number == 3:
        return "x <= 0, y <= 0"
    elif number == 4:
        return "x >= 0, y <= 0"

print(answer(3))