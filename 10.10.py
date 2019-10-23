# -*-encoding:utf-8-*-
# author:dlgamelb

import json
import requests

"""
xml和json互转：xmltodict.parse()xml转json;xmltodict.unparse()json转xml
"""
import xmltodict

"""
序列化：把python的数据类型转化为str的类型过程
反序列化：把str的类型转化为python的数据类型
"""

dict1 = {'internationalAreaCode': '+86', 'persistenceHint': True, 'phoneNumber': 11111111111, 'publicKey': 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCROXqyCKxG8DrQKvrmdwiAHFJseaLHKsdzJ+61EpEGUawyLk5obn2Z2lyVVGjqT3KECk3DJtAD6Jux/m/gW2/lxspvhUO1YE1P8OZuUq5xhr/3AWuSSXCqLM2q6TEMnI2VE1BzlsRcxQVGVd4kGszzpyLXYS9ubFTTp1C2A+uZ1QIDAQAB', 'rsaPassword': 'TPBt42C4NaEznv76SAuospae/WvRcNEJf0ca5Ny5lni5T24X+57ki2Pc1FWpcoJEiBXUaGtB2tGW0SSqCSLSujFufdr5ZQRheUvVRRsZhVE9Q43DtNYDCrs5HUZ8bYOaCYbrByxTcPNWCfLOINwjaLifyUhghSzEyQUGcaOMaqo='}


#print(type(dict1))


r = requests.post(url='https://www.fxiaoke.com/FHH/EM0HUL/Authorize/PersonalLogin?_fs_token=', data=json.dumps(dict1), headers={'Content-Type': 'application/json'})

print(r.text, type(r.text))
xml_json = xmltodict.parse(r.text)
print(xml_json, type(xml_json))



"""
字典的序列化和反序列化
"""
dict2 = {'name': 'chenguo', 'age': '18'}

# 序列化：dict-->str
dict_str = json.dumps(dict2)
print('序列化后的结果信息：')
print(dict_str, type(dict_str))

# 反序列化：str-->dict
str_dict = json.loads(dict_str)
print('反序列化后的结果信息：')
print(str_dict, type(str_dict))


"""
列表的系列化和反序列化
"""
list1 = ['chenguo', 'fangfang', 'xiaoming']
# 序列化：list-->str
list_str = json.dumps(list1)
print('序列化后的结果是：')
print(list_str, type(list_str))

# 反序列化：str-->list
str_list = json.loads(list_str)
print('反序列化的结果是:')
print(str_list, type(str_list))


"""
元组的序列化和反序列化的过程
"""
tuple1 = (1, 2, 3)
# 序列化
tuple_str = json.dumps(tuple1)
print('序列化后的结果是：')
print(tuple_str, type(tuple_str))
# 反序列化
str_tuple = json.loads(tuple_str)
print('反序列化后的结果是：')
print(str_tuple, type(str_tuple))
