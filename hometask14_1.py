# hometask_14_1
# Создать класс Dog.
# Класс имеет четыре
# атрибута: height, weight, name, age. Класс
# имеет три метода: jump, run, bark. Каждый
# метод выводит сообщение на экран.
# Создать объект класса Dog, вызвать все
# методы объекта и вывести на экран все его
# атрибуты.


class Dog:
    def __init__(self,height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self, jump):
        print(f'Собачка прыгает на {jump} метров')

    def run(self, run):
        print(f'Собачка бегает со скоростью {run} км/ч')

    def bark(self, bark):
        print(f'Собачка лает с громкостью {bark} дБ')

shepherd_dog = Dog(1,8,'Vasya',4)

print(shepherd_dog.jump(1),shepherd_dog.run(1),shepherd_dog.bark(1))
print(shepherd_dog.height,shepherd_dog.weight,shepherd_dog.name,shepherd_dog.age)

# hometask_14_2
# Добавить в класс Dog метод change_name.
# Метод
# принимает на вход новое имя и меняет
# атрибут имени у
# объекта. Создать один объект класса.
# Вывести имя.
# Вызвать метод change_name. Вывести имя.

class Dog:
    def __init__(self,height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self, jump):
        print(f'Собачка прыгает на {jump} метров')

    def run(self, run):
        print(f'Собачка бегает со скоростью {run} км/ч')

    def bark(self, bark):
        print(f'Собачка лает с громкостью {bark} дБ')

    def change_name(self, new_name):
        self.name = new_name
#        return new_name


shepherd_dog = Dog(1,8,'Vasya',4)

print(shepherd_dog.name)

print(shepherd_dog.change_name('Katya'))