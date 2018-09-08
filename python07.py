class Student:
    def __init__(self, code, name,age):
        self.code = code
        self.name = name
        self.age = age

    code = '001'
    name = '222'
    __age = 13

    def display(self):
        return self.code + self.name + '年龄' + str(self.age)