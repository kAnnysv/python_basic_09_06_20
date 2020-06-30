name_f = input('Введите имя файла: ')
f = open(name_f, 'w')
while True:
    strc = input('Введите стрку: ')
    if strc == '':
        break

    f.write(strc + '\n')

f.close()
