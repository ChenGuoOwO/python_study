# encoding: utf-8
# author:cg


def login(username='chenguo', password='chenguo'):
    if username == 'chenguo' and password == 'chenguo':
        return 'sdkfjs'
    else:
        return '登录错误'


def profile(token):
    if token == 'sdkfjs':
        return '欢迎'
    else:
        return '请登录'


def f3():
    def f4():
        return'hello'
    return f4()


print(f3())
print(profile(login()))

