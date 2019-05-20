
class A:
    def show(self):
        print("A Show")

class B(A):
    def show(self):
        print("B Show")

b=B()
b.show()
