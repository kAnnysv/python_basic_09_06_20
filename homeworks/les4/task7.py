def fact(n):
    i = 1
    res = 1
    while i <= n:
        res = res * i
        yield res
        i += 1


if __name__ == '__main__':
    n = input('Введите целое число: ')
    n = int(n)
    for el in fact(n):

        print(el)

