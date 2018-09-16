class Student:
    def __init__(self, code, name,age):
        self.code = code
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.name;

    @property
    def name(self,name):
        self.name = name;    

    def display(self):
        return self.code + self.name + '年龄' + str(self.age)