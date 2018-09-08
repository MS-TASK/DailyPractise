a,b = 0,1
while b < 20:
    print(a,end= " ")
    n = b
    b = a + b
    a = n

languages = ["x", "y", "z", "q"]
for x in languages:
    if x != "y":
        print(x,end="-")
        continue
    print("over !")

var1 = list(range(6))
print(var1)

it = iter(var1)
print(next(it))
print(next(it))

for x in it:
    print(x,end=" ")

# 函数定义，可变参数以 * 导入转换成tuple,** 转换成 字典
# 

var2 = [2,4,6]
var3 = [3*x for x in var2]
print(var3)    

var3 = [[x,3*x] for x in var2]
print(var3)


