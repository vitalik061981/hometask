# Hometask_13_3
# Напишите функцию которая
# принимает на вход список
# целых чисел, удаляет из него
# все нечётные значения, а
# чётные нацело делит на два.
# In: 852 85 784 58
# Out: [426, 382, 29]
nums = [int(i) for i in input().split()]

def even(nums):

    a = []

    for i in nums:
        if i % 2 == 0:
            i = i / 2
            a.append(int(i))
    return a

print(even(nums))

# Hometask_13_2
# Напишите функцию f(x), которая
# возвращает значение следующей
# функции, определённой на всей
# числовой прямой:
# In: 4.5
# Out: 7.25

x = float(input())

def y(x):

    if x <= -2:
        y = 1 - (x + 2)**2

    if -2 < x <= 2:
        y = - x / 2

    if x > 2:
        y = (x - 2)**2 + 1

    return y

print(y(x))

# Hometask_13_1
# Из полученного списка чисел
# создайте список с суммами
# этих чисел, отсортированными
# по возрастанию
# In: 965 582 023 8 695210
# Out: [5, 8, 15, 20, 23]

nums = [int(i) for i in input().split()]

d = []
for i in nums:
    b = []

    while i > 0:
        b.append(i % 10)
        i = i // 10

    c = sum(b)
    d.append(c)

d.sort()
print(d)

# 2 ВАРИАНТ

nums = [int(i) for i in input().split()]

def lst1(nums):
    d = []
    for i in nums:
        b = []

        while i > 0:
            b.append(i % 10)
            i = i // 10

        c = sum(b)
        d.append(c)

    d.sort()
    print(d)

lst1(nums)