num_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res = []
""" Цикл for помог алгоритм генератора понять
 """

for el in range(1, len(num_list)):
    if num_list[el] > num_list[el - 1]:
        res.append(num_list[el])
print(res)
""""генератор списка"""

res_list = [num_list[el] for el in range(1, len(num_list)) if num_list[el] > num_list[el - 1]]

print(res_list)
