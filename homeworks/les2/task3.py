n = int(input('Введите номер месяца от 1 до 12: '))
# Почему неработает while n < 1 and n >12: ?
while True:
    if n < 1:
        n = int(input('Введите номер месяца от 1 до 12: '))
    elif n > 12:
        n = int(input('Введите номер месяца от 1 до 12: '))
    else:
        n = str(n)
        break
my_dict = {'1': 'winter', '2': 'winter', '3': 'spring', '4': 'spring', '5': 'spring', '6': 'sammer',
           '7': 'sammer', '8': 'sammer', '9': 'fall', '10': 'fall', '11': 'fall', '12': 'winter'}
print(my_dict.get(n))
my_list = ['winter', 'winter', 'spring', 'spring', 'spring', 'sammer', 'sammer', 'sammer', 'fall', 'fall',
           'fall',
           'winter']
n = int(n)
print(my_list[n - 1])
