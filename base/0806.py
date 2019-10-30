# encoding: utf-8
# author:cg


'''
需求：要求注册账户，然后注册的账户登录到系统后，显示出登录的昵称
1、注册的函数
2、登录的函数
3、获取昵称的函数
'''


def register():
    '''实现账户的注册功能'''
    username = input('请输入账号：')
    password = input('请输入密码：')
    temp = username+'|'+password
    with open('login.md', 'w') as f:
        f.write(temp)


# register()


def login():
    '''登录的函数'''
    username = input('请输入账户：')
    password = input('请输入密码：')
    with open('login.md', 'r') as f:
        info = f.read()
    info = info.split('|')
    if username == info[0] and password == info[1]:
        return True
    else:
        return False


# print(login())


def getNick(func):
    '''获取昵称'''
    with open('login.md', 'r') as f:
        info = f.read()
    info = info.split('|')
    if func:
        print('{}您好，欢迎您访问无涯课堂'.format(info[0]))
    else:
        print('请登录系统')


# getNick(login())


'''
format:str.fotmat()
基本语法是通过 {} 和 : 来代替以前的 % 
'''


if __name__ == '__main__':
    while True:
        t = int(input('1、注册 2、登录 3、退出系统\n'))
        if t == 1:
            register()
        elif t == 2:
            getNick(login())
        elif t == 3:
            import sys
            sys.exit(1)
        else:
            print('输入错误，请继续')
            continue

