def my_func(x, y):
    abc = abs(y)
    n = 1
    res = x
    while n < abc:
        res = (res * x)
        n = n + 1
    ext = 1 / res
    return ext


print(my_func(2, -10))
