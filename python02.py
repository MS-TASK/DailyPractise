import sys

print("命令行参数为：")
for i in sys.argv:
    print(i)

print("\n python 路径为", sys.path)

str = 'Runoobxx12'

print(str)
print(str[0:-1])

str2 = "sud"
print(str2[0:-2])

# 不换行输出
print(str * 2, end=" ")
print(str[2:])
print(str2)
"""
# python
Number : int float bool complex
String : str[0:-2] 第一个到倒数第三个的字符 * 重复字符串
Tuple(数组) :
List: list[0:-1]
Dictionary:
Set:
"""

var1 = 1
var2 = 2

# 删除对象引用
del var1, var2

print('Ru\noob')

list = ['abcd', 786, 2.23, 'runoob', 70.2]
print(list)
print(list[0])
print(list[1:3])
print(list[1:])
print(list * 2)
print(list + list)

tup = (1,2,3,4)
print(tup[0])
print(tup[1:5])

setStr={'a','b','c','d'}
print(setStr)

exists = 'a' in setStr
print(exists)

setA = set('abracadabra')
setB = set('a123213')
print(setA)

print(setA - setB)
print(setA | setB)
print(setA & setB)
print(setA ^ setB)

# dict

dictStr = {}
dictStr['one'] = "1"
dictStr[2] = "2"

ss = dict(a=1,b=2,c=3)
print(ss)

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print(dictStr['one'])
print(dictStr[2])
print(tinydict.keys())
print(tinydict.values())

tinydict.pop('name')
print(tinydict)


