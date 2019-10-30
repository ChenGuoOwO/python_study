# -*-encoding:utf-8-*-
# author:dlgamelb

import requests
import json
import hashlib
from urllib import parse


#res = requests.get(url='')
#assert res.text


# 文件的序列化和反序列化

r = requests.get(url='http://www.weather.com.cn/data/sk/101190408')

# 对文件进行序列化-->把服务端的响应数据写到文件中

json.dump(r.content.decode('utf-8'), open('weather.json', 'w'))

# 对文件的反序列化：就是读取文件的内容
"""
1.文件反序列化后，类型是unicode
2.进行编码，把unicode类型转化为str类型
3.然后使用反序列化，把str转化为字典类型
"""
# dict1 = json.loads(json.load(open('weather.json', 'r'))).encode('utf-8')
dict1 = json.load(open('weather.json', 'r'))
print(dict1, type(dict1))
# print(dict1['weatherinfo']['city'])


"""
1.对请求参数做ascill码的排序
2.做URL encode编码:name=chenguo&age=18&city=wuhan&work=tester
3.做md5加密-->sign
"""

dict2 = {'name': 'chenguo', 'age': 18, 'city': 'wuhan', 'work': 'tester'}
dicts = {'name': 'chenguo', 'age': 18, 'city': 'wuhan', 'work': 'tester', 'sign': 'sign'}

dict2 = dict(sorted(dict2.items(), key=lambda item: item[0]))
print(dict2)

datas = parse.urlencode(dict2)
print(datas)

md5 = hashlib.md5()
md5.update(datas.encode('utf-8'))
print(md5.hexdigest())


def getMd5(**kwargs):
    dict3 = dict(sorted(kwargs.items(), key = lambda item: item[0]))
    data1 = parse.urlencode(dict3)
    md = hashlib.md5()
    md.update(data1.encode('utf-8'))
    return md5.hexdigest()


print(getMd5(name='haha', ghj='hangzhou'))

