number = input('Ведите число: ')
array1 = list(number)
array = array1[:]
i = 0
while i < len(array):
    if array[i] < array[i + 1]:
        array.remove(i)
    else:
        array.remove(i + 1)
print(array)
