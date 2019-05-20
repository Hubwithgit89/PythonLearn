
class Temp:



    def sum(self):
        return  "sum"

    def sum(self,a,b):
        return  a+b

    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        elif a!=None:
            s=a
        else:
            s="No value"
        return s
t=Temp()
print(t.sum())
