def div(a, b):
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        print('На 0 делить нельзя')
num1 = int(input('Введите делимое: '))
num2 = int(input('Введите делитель: '))
res = div(num1,num2)
print(res)