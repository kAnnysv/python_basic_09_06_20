rev = input('Введите выручку: ')
rev = int(rev)
exp = input('Введите расходы: ')
exp = int(exp)
result = rev - exp
if result >= 0:
    print(f'Ваша прибыль {result}')
else:
    print(f'Ваш убыток {result}')

per = input('Введите количество работников: ')
per = int(per)
effect = result / per
if result >= 0:
    print(f'{effect} прибыли на 1 сотрудника')
else:
    print(f'{effect} убытков на одного сотрудника')
