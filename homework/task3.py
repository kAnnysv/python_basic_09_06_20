from statistics import mean

with open('pers_txt', 'w') as f:
    f.write('Jon 20\n')
    f.write('Sam 26\n')
    f.write('Jak 30\n')
    f.write('Sara 15\n')
    """"Пребразуем строки файла в словарь"""
pers = {}
with open('pers_txt') as file:
    for line in file:
        key, value = line.split()
        pers[key] = int(value)
salary_low = {}
for name, salary in pers.items():
    if salary < 20:
        salary_low.update({name: salary})

print(f'Зарплата меньше 20 у {salary_low}')

""""Создаем список зарплат"""

sel = pers.values()
means = mean(sel)
print(f'Средня зарплата {means}')
