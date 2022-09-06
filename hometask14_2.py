# 14_8 14_9
# Создайте класс для салона
# красоты, чтобы можно было
# создавать дома с салоном
# красоты.
# Методы:
# - Маникюр
# - Стрижка
# Методы прописывать не надо,
# просто поставьте заглушку
# Добавьте в салон красоты метод
# salon_opening_hours, который
# сообщает салон открыт или
# закрыт.
# Создайте дом с салоном красоты.
# Атрибуты:
# Час открытия салона
# Час закрытия салона
# Посмотрите работает ли салон в
# 13 часов, а в 23?
#
# 14_8 14_9
# класс салон красоты - миксин
# методы:
# - маникюр
# - стрижка
# - время работы
#
# создать класс дом с салоном красоты (наслелование)
# атрибуты:
# - время открытия
# - время закрытия
#
# вызвать метод в 13 часов, в 23

class Building:
    def __init__(self, doors, windows, floors):
        self.doors = doors
        self.windows = windows
        self.floors = floors

    def build(self):
        print("The building was built")

    def destroy(self):
        print("The building was destroyed")


class BeatifulSalonMixin:
    def manikur(manikur):
        print(f'салон крастоты {manikur}')

    def strigka(strigka):
        print(f'салон крастоты {strigka}')

    def timework(timework):
        print(f'салон крастоты {timework}')

    def salon_opening_hours(time):
        if time > 8 and time < 22:
            print('салон открыт')
        else:
            print('салон закрыт')


class HouseWithBeatifulSalon(Building,BeatifulSalonMixin):
    def __init__(self,doors, windows, floors, topen,tclose):
        super().__init__(doors, windows, floors)
        self.topen = topen
        self.tclose = tclose

b = BeatifulSalonMixin.salon_opening_hours(13)
c = HouseWithBeatifulSalon.salon_opening_hours(23)

print(b)
print(c)
print()


