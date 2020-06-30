f = open('tas2.txt', 'w')
f.write('str123\n')
f.write('str text 456\n')
f.write('sdfg fgt5\n')
f.close()
lin = 0
words = 0
fw = []
"""Количество строк можно посчитать так"""
for strc in open('tas2.txt'):
    fw.append(strc)
    lin += 1
print(f'Количество строк {lin}')
"""Количество слов в каждой строке"""
i = 0
for el in fw:
    a = el.split(' ')
    i += 1
    print(f'cтрока {i} - слов {len(a)}')
