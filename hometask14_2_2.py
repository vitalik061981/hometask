# Hometask_14_5
# Создать три класса: Dog, Cat, Parrot.
# Атрибуты каждого класса: name, age,
# master.
# Каждый класс содержит
# конструктор и методы: run, jump,
# birthday(увеличивает age на 1), sleep.
# Класс Parrot имеет дополнительный
# метод fly, Cat - meow, Dog - bark.
# Hometask_14_6
# Создать родительский класс Pet,
# содержащий все общие методы
# классов
# Dog, Cat, Parrot. Унаследовать Dog,
# Cat, Parrot от класса Pet. Удалить в
# дочерних классах те методы, которые
# имеются у родительского класса.
# Создать объект каждого класса и
# вызвать все его методы

class Pet:
    def __init__(self,name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def jump(self, jump):
        print(f'прыгает на {jump} метров')

    def run(self, run):
        print(f'бегает со скоростью {run} км/ч')

    def birthday(self, birthday):
        self.age += 1
        print(f'Рождение {birth}')

    def sleep(self, sleep):
        self.sleep = sleep
        print(f'животное {sleep} дБ')

class Dog(Pet):
    def __init__(self,name,age,master):
        super( ).__init__(name,age,master)
        print('Dog')

    def bark(self):
        print('bark')

class Cat(Pet):
    def __init__(self,name,age,master):
        super( ).__init__(name, age, master)
        print('Cat')

    def meow(self):
        print('meow')

class Parrot(Pet):
    def __init__(self,name,age,master):
        super( ).__init__(name, age, master)
        print('Parrot')

    def fly(self):
        print('fly')

dogg = Dog(10,20,10)
dogg.bark( )
dogg.jump('1')
dogg.run('1')
dogg.birthday('1')

catt = Cat(10,20,10)
catt.meow( )
catt.jump('1')
catt.run('1')
catt.birthday('1')

parott = Parrot(10,20,10)
parott.fly( )
parott.jump('1')
parott.run('1')
parott.birthday('1')