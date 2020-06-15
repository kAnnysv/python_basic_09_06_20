my_str = input('Введите строку: ')
result = my_str.split()
for idb, itm in enumerate(result, 1):

    print(idb, itm[:10])


