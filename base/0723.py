#encoding: utf-8
#author:cg


list1 = [44, 55, 66, 88]
print(len(list1))
print(min(list1))
print(max(list1))

age = 6
print('true') if age > 5 else print('false')

login = lambda username, password: print('登录 成功')if username == 'chenguo' and password == 'chenguo'else print('登录错误')


print(login('chenguo', 'chenguo'))


data = lambda **kwargs: dict(sorted(kwargs.items(), key=lambda item: item[0]))

print(data(name= 'chenguo', age=18))