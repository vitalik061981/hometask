# exam_3_1
# Напишите функцию, которая
# будет принимать номер
# кредитной карты и показывать
# только последние 4 цифры.
# Остальные цифры должны
# заменяться звездочками
#
def name1(nname):

    c = []
    for j in nname[:12]:
        j = '*'
        c.append(j)
    for i in nname[12:]:
        c.append(i)

    return c

nname = input('')

print(name1(nname))
print(' '.join(name1(nname)))

# exam_3_2
# Напишите функцию, которая
# проверяет: является ли слово
# палиндромом

def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True

print(isPalindrome('summer'))
print(isPalindrome('шалаш'))

# exam_3_3
# Напишите классы Круг,
# Прямоугольник, Квадрат.
# Каждый класс должен
# содержать метод нахождения
# площади фигуры.
# Используйте:
# - Наследование
# - Абстрактный класс
# и методы
# - Округлите площадь круга до 2х чисел после запятой
# - Число π возьмите из модуля
# math

from abc import ABC, abstractmethod
import math

class Figuri(ABC):

    @abstractmethod
    def ploshad(self):
        pass

class Krug(Figuri):

    def __init__(self, radius):
        self.radius = radius

    def ploshad(self):
        return round((self.radius ** 2) * math.pi, 2)

class Pryamougolnik(Figuri):

    def __init__(self, a,b):
        self.a = a
        self.b = b

    def ploshad(self):
        return round(self.a * self.b, 2)

class Kvadrat(Figuri):

    def __init__(self, c):
        self.c = c

    def ploshad(self):
        return round(self.c * self.c, 2)

kvadrat_ploshad = Kvadrat(32)
krug_ploshad = Krug(30)
pryamougolnik_ploshad= Pryamougolnik(54,56)
ploshadd = [kvadrat_ploshad,krug_ploshad,pryamougolnik_ploshad]
for i in ploshadd:
    print(i.ploshad())

