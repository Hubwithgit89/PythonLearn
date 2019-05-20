class Student:
    def __init__(self,name,rollNo):
        self.name=name
        self.rollNo=rollNo
        self.lap=self.Laptop()

    def show(self):
        print(self.name,self.rollNo)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand="Dell"
            self.cpu="i5"
            self.ram="16GB"

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=Student("abc",123)
s2=Student("xyz",456)
s1.show()

lap1=s1.lap
lap2=Student.Laptop()
lap2.show()
