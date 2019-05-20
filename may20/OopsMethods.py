
class Student:

    company="infoview"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return ((self.m1+self.m2+self.m3)/3)

    @classmethod
    def getName(cls):
        #cls is to use class variable
        return (cls.company)


    @staticmethod
    def info():
        return "student data"

s1=Student(3,3,35)
s2=Student(34,646,46)

#INSTANCE method(Passing self)
s1.avg()
s2.avg()
print(s1.avg())

#CLASS METHOD
print(Student.getName())

#STATIC method
print(Student.info())

#s1.info()







