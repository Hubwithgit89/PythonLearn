#GLOBAL KEYWORD
a=10
print(id(a))
def test():
    #global a
    a=15
    print(id(a))
    print("in fun = ",a)

test()
print(id(a))
print("out ",a)
