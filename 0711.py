# encoding: utf-8
# author:cg


list1 = [1, 2, 3, 5, 10]
list2 = [8, 10, 20, 102]


def pl1():
    print(list1)


def pl2():
    print(list2)


list1.append(11)
pl1()

list1.insert(0, 10)
pl1()

print(list1.count(10))

print(list1.index(11))

list1.pop()
