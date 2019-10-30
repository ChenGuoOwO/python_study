# -*-encoding:utf-8-*-
# author:dlgamelb

"""
iterables & generators
"""


def f():
    list1 = []
    for x in range(5):
        x += 1
        list1.append(x)
    return list1


print(f())

