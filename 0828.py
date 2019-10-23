# -*-encoding:utf-8-*-
# author:dlgamelb


def get():
    m = 0
    n = 2
    l = ['s', 1, 3]
    k = {1: 1, 2: 2}
    p = ('2', 's', 't')
    while True:
        m += 1
        yield m
        yield m, n, l, k, p


it = get()
print(it)
print(next(it))  # 1
print(next(it))  # (1, 2, ['s', 1, 3], {1: 1, 2: 2}, ('2', 's', 't'))

print(next(it))  # 2
print(next(it))
print(type(next(it)))  # <class 'tuple'>
print(next(it))
print(next(it))
