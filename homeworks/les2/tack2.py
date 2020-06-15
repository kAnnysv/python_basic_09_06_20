user = input('Введите элементы списка через пробел: ')

my_list = user.split()
if len(my_list) % 2 != 0:
    lost = my_list[len(my_list) - 1]
    my_list.pop()
    for el in range(0, len(my_list), 2):
        my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    my_list.append(lost)
else:
    for el in range(0, len(my_list), 2):
        my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]

print(my_list)
