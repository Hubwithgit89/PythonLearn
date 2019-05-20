
class A:
    def disp1(self):
        print("Disp 1")

    def disp2(self):
        print("Disp 2")

class B:
    def disp1(self):
        print("Disp 3")

    def disp4(self):
        print("Disp 4")

class C(A,B):
    def disp5(self):
        print("disp 5")


c=C()
c.disp1()