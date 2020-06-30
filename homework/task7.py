from sys import argv
from statistics import mean
import json

"""Функция преобразования строк  в float"""


def fl_list(s):
    fl_s = []
    for el in s:
        try:
            el = float(el)
        except ValueError:
            s.remove(el)
    for el in s:
        el = float(el)
        fl_s.append(el)
    return fl_s


if __name__ == '__main__':
    with open('report.txt', 'w') as f:
        f.write('firm_1 ooo 10000 5000.\n')
        f.write('firm_2 ooo 10000 7000.\n')
        f.write('firm_3 ooo 10000 15000.\n')
        """"Создание словаря"""
rep = {}
with open('report.txt') as f:
    for line in f:
        key, *value = line.split()
        rep[key] = value
        """"Преобразую словари в float"""

f1 = fl_list(rep.get('firm_1'))
f2 = fl_list(rep.get('firm_2'))
f3 = fl_list(rep.get('firm_3'))

profit_f1 = (f1[0] - f1[1])
profit_f2 = (f2[0] - f2[1])
profit_f3 = (f3[0] - f3[1])
print(f'Прибыль firm_1 {profit_f1}, firm_2 {profit_f2}, firm_3 {profit_f3}')
profit_list = [profit_f1, profit_f2, profit_f3]
average_profit = mean([el for el in profit_list if el > 0])

print(f'Прибыль группы без убыточных компаний {average_profit}')
result = [{'firm_1': profit_f1, 'firm_2': profit_f2, 'firm_3': profit_f3},
          {'average_profit': mean(profit_list)}]
print(result)

with open('report.json', 'w') as f:
    json.dump(result, f)
