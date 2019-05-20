class Car:
    #CLASS VARIABLE
    wheels=4

    def __init__(self):
        #INSTANCE variable
        self.mileage=10
        self.company="BMW"

c1=Car()
c2=Car()
print(c1.company,c1.mileage,c1.wheels)
print(c2.company,c2.mileage,c2.wheels)

c1.mileage=30
print(c1.company,c1.mileage,c1.wheels)
print(c2.company,c2.mileage,c2.wheels)

Car.wheels=5
print(c1.company,c1.mileage,c1.wheels)
print(c2.company,c2.mileage,c2.wheels)