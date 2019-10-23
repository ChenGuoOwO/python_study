# -*-encoding:utf-8-*-
# author:dlgamelb

import time as t
import os
import sys

print(dir(t))

# 获取时间戳
print(int(t.time()))

# 获取当前时间
print(t.localtime(t.time()))
print(t.strftime('%y-%m-%d %H:%M:%S', t.localtime()))


print(dir(os))
# 当前目录
print(u'当前文件的目录', os.path.dirname(__file__))

# 当前文件的上级目录
print(u'文件当前目录的上级目录', os.path.dirname(os.path.dirname(__file__)))


print(os.path.abspath(__file__))


# 实现对d:/wb.chenguo/python_study/test/01.txt文件内容的读取
base_dir = os.path.dirname(__file__)

print(base_dir)

f = open(os.path.join(base_dir, 'test/01.txt'), 'r')
print(f.read())

# join连接字符串数组；os.path.join()将多个路径组合后返回
print('\n'.join([' '.join('%sx%s=%-2s' % (x, y, x*y) for x in range(1, y+1)) for y in range(1, 10)]))


# 请求参数是不确定的，可能有一个，可能有N个
def f(*args, **kwargs):
    return kwargs

print(f(name = 'cc', age = '18'))


"""
1.标准库：python37\Lib
2.第三方的库：python37\lib\site-packages
3.自定义的库
"""
for item in sys.path:
    print(item)


sys.path.append('D:\wb.chenguo\python_study')

print(item)

import  request


