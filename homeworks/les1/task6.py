a = input('Кол-во км в первый день: ')
a = int(a)
b = input('Нужное кол-во км: ')
b = int(b)
i = 1
km = (a + a / 10)
while i >= b:
    km = (km + km / 10)
    print(f'{i}-й день: {km}/n')
    i += 1
