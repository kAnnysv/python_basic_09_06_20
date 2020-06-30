with open('num_sum.txt', 'w') as f:
    f.write('33 45 3 6')
with open('num_sum.txt', 'r') as num_f:
    for line in num_f:
        sn = line.split()
int_sn = [int(el) for el in sn]
sum_sn = sum(int_sn)
print(f'Сумма чисел файла {sum_sn}')
