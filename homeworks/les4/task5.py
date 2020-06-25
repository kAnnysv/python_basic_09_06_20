from functools import reduce

num_list = [el for el in range(100, 1001) if el % 2 == 0]


def list_sum(a, b):
    return a + b


print(reduce(list_sum, num_list))
