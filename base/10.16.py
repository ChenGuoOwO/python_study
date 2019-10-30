# -*-encoding:utf-8-*-
# author:dlgamelb


def div(a, b):
    return a/b


#div(1, 0)

"""
1.try代码执行正常,就不会执行expect的代码
2.只有try代码执行异常，就会执行expect的代码
"""
try:
    div(1, 0)
except ZeroDivisionError as e:
    print(e.args)


def f(*args, **kwargs):
    return