# Классы
class Gun():
    """Описание пушки"""
    def __init__(self, number_gun, kalibr):
        """Свойства пушки"""
        self.number_gun = number_gun
        self.kalibr = kalibr
        self.age = 0
    
    def made(self):
        """Создает пушку"""
        print("Пушка " + str(self.number_gun) + " калибром " + str(self.kalibr) + " готова!")
    def age_of_gun(self, year):
        """Возраст пушки"""
        self.age += year

gun1 = Gun(1, 20)
gun2 = Gun(2, 15)

print(gun2.kalibr) # - обращение к свойствам класса
gun1.made() # - обращение к методам класса
print(gun1.age)
gun2.age_of_gun(5)
print(gun2.age) 
print(gun1.age)

# Наследование
class Pistol (Gun):
    """Пистолеты"""
    def __init__(self, cahs, kalibr):
        super().__init__(self, kalibr)
        self.cash = cahs

makar = Pistol(7, 12)
print(makar.kalibr)