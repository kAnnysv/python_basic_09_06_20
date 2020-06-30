from sys import argv
"""Функция извлечения чисел из сторки, но если в строке чисел нет, 
то не работает. Не хватило времени доработать
"""

def int_list(s):
    digits = []
    try:
        for symbol in s:
            if '1234567890'.find(symbol) != -1:
                digits.append(symbol)
                result = int((''.join(digits)))
        return result

    except NameError:
        return digits





if __name__ == '__main__':

    with open('less.txt', 'w', encoding='UTF-8') as f:
        f.write('Информатика: 100(л) 50(пр) 20(л)\n')
        f.write('Физика: 30(л) - 10(лаб)\n')
        f.write('Физкультура: - 30(пр) - \n')
    less = {}
    with open('less.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            key, *value = line.split()
            less[key] = value
        print(less)
    inf = sum([int_list(el) for el in less.get('Информатика:')])
    print(f'Занятий по информатике {inf}')
    #phys = sum([int_list(el) for el in less.get('Физика:')])
    # sport = sum([int_list(el) for el in less.get('Физкультура:')])
""""Поэтому посчитал тоько информатику"""