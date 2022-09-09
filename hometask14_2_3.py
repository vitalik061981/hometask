# Установите статичечкий атрибут
# мин цена в салоне красоты
# Допишите методы.
# Маникюр стоит на 20% больше
# Стрижка зависит от длины
# волос:
# меньше 30см - +20%,
# От 30 до 50 см - +50%
# Свыше 50 см - +80%

class BeautySaloon:
    
    min_price = 10

    # def __init__(self,min_price):
    #     self.min_price = min_price


    def manicury (self,min_price):
        manicury_price = min_price * 1,2


    def ahaircut(self,min_price,hair_length):
        self.hair_length = hair_length
        if hair_length < 30:
            ahaircut_price = min_price * 1,2
        elif hair_length > 30 and hair_length < 50:
            ahaircut_price = min_price * 1,5
        elif hair_length > 50:
            ahaircut_price = min_price * 1,8
        return ahaircut_price


bs1 = BeautySaloon()
bs1.manicury(12)

bs2 = BeautySaloon()

print(bs2.ahaircut(15,34))
