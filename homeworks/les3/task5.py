suma = 0
el = 0
while el != 'q':
    user_number = input('Введите числа разделеные '
                        'пробелом,знак q останавливает программу : ')
    res = user_number.split()
    for el in res:
        if el == 'q':
            break
        else:
            el = int(el)
            suma = suma + el
    print(suma)
