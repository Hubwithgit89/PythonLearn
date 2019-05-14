#FUNCTION WITH MUTABLE AND IMMUTABLE ARGUMENTS
def update_Int(x):
    print("id in before update = ",id(x))
    x=8
    print("id in after update = ",id(x))
    print("x= ",x)
a=10
print(id(a))
update_Int(a)
print("a== ",a)
#*****************************************************
print(20*"*")
#****************************************************
def update_List(blst):
    print("id in before update = ",id(blst))
    blst[1]=15
    print("id in after update = ",id(blst))
    print("blst= ",blst)
alist=[10,20,30]
print(id(alist))
update_List(alist)
print("alst= ",alist)
