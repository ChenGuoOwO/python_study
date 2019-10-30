# encoding: utf-8
# author:cg


'''
*args 可变位置参数 返回元组
**kwargs 可变关键字参数 返回字典
'''

list1 = [1, 2, 3, 4, 5]


def f():
    list2 = []
    for i in list1:
        i += 100
        list2.append(i)
    return list2


print(f())


def f(a):
    return a+100


print(list(map(f, list1)))

print(list(map(lambda a: a+100, list1)))


def f():
    list2 = []
    for i in list1:
        if i > 1:
            list2.append(i)
    print(list2)


f()


print(list(filter(lambda b: b > 1, list1)))

'''
1.函数可以作为一个变量
2.函数的参数也可以是函数
3.函数是可以嵌套的
'''


def a():
    print('hello')


def f2(a):
    return a


f2(a())
