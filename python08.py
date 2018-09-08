from python07 import Student

class newStudent(Student):
    gender = ''

    def __init__(self,code,name,gender):
        Student.__init__(self,code,name,18)
        self.gender = gender

    def display(self):
        print("%s 年龄 %d 性别 %s"%(self.name,self.age,self.gender))
    

s = newStudent('002','Tom','男')
s.display()

superStr = super(newStudent,s).display()
print(superStr)