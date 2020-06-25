from itertools import count, cycle

for x in count(10):
    if x > 67:
        break
    else:
        print(x)

n = 0
for x in cycle('1FH6'):
    if n < 8:
        print(x)
        n += 1
    else:
        break
