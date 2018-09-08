import python04
import os

print(dir(python04))

print(os.getcwd())

print(os.listdir())


f = open('E:\\python\\DailyPractise\\test.txt','r',encoding='utf-8')
# print(f.read())

for line in f:
    print(line)

f.close()