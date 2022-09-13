# exam_1
# напишите функцию,которая будет принимать фамилию
# и показывать только первую букву.Буква
# должна быть заглавной.Остальные буквы
# должны заменяться звездочкой

def name1(nname):

    c = []
    for j in nname[:1]:
        c.append(j)
    for i in nname[1:]:
        i = '*'
        c.append(i)

    return c

nname = input('')
b = nname.capitalize()

print(name1(b))
print(' '.join(name1(b)))

# Hometask_14_8
# Добавьте в класс Pet дескриптор,
# чтобы нельзя было задать
# отрицательный возраст или 0

class NonNegativeValue:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"{self.name} cannot be negative")
        instance.__dict__[self.name] = value

class Pet:
    age = NonNegativeValue()
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

a = Pet("apples", -2.15, 2)
print(a)

# Hometask_14_9
# Добавьте в класс Pet валидацию,
# чтобы у питомца было имя и хозяин

class Pet:
    def __init__(self,name, age, master):
        self.__name = name
        self.age = age
        self.__master = master

    def set_name(self,name):
        if name <= 0:
            raise ValueError('Нет имени')
        self.__name=name

    def set_master(self,master):
        if master <= 0:
            raise ValueError('Нет хозяина')
        self.__master=master

dogg = Pet(10,-20,10)
print(dogg.set_name(-20))
print(dogg.set_master(-20))