# exam_2
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
