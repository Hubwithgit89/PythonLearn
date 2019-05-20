 #constructor in inheritance



class A:

    def __init__(self):
        print("A init")

    def disp1(self):
        print("Disp 1")

    def disp2(self):
        print("Disp 2")

class B:
    def __init__(self):
        print("B Init")

    def disp1(self):
        print("Disp 3")

    def disp4(self):
        print("Disp 4")

#b=B()


class C(A,B):
    def __init__(self):
        super().__init__()
        print("C init")

    def disp5(self):
        print("disp 5")


c=C()
#c.disp1()