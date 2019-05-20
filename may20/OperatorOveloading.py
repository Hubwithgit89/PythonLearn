
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        return Student(m1,m2)
    def __str__(self):
        return "{},{}".format(self.m1,self.m2)

s1=Student(22,33)
s2=Student(44,66)
s3=s1 + s2
print(s3.m1,s3.m2)

print(s1)

