from sys import argv

name, work_hours, cost_hour = argv
print(name)
work_hours = int(work_hours)
cost_hour = int(cost_hour)
print('Выработано часов: ', work_hours)
print('Ставка в час: ', cost_hour)
sum = work_hours * cost_hour

print('Премия: ', sum / 10)
print('Зарплата: ', sum + sum / 10)
