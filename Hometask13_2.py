# Hometask_13_4
# Напишите функцию, которая
# создает список случайных
# элементов. На фход функция
# принимает кол-во элементов,
# минимальное и максимальное
# значение
# In: rand_nums(7, 2, 12)
# Out: [12, 6, 9, 2, 11, 5, 8]

import random

n = int(input())
minn = int(input())
maxx = int(input())

def rand_nums(n, minn, maxx):
    ls = [random.randint(minn, maxx) for i in range(n)]
    return ls

print(rand_nums(n, minn, maxx))

# Пользователь делает вклад N
# рублей на X лет под 10 %
# годовых, т.е. каждый год размер
# его вклада увеличивается на
# 10%. Напишите функцию,
# которая возвращает
# накопленную сумму.
# In: bank(200, 4)
# Out: 292.82

n = int(input())
x = int(input())

def bank(x):
    depo= 1.1**x
    a = format(n*depo, '.2f')
    return a

print(bank(x))

#a = float('{:.2f}'.format(bank(x)))
