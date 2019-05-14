#Function with  two return value
def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

result1,result2=add_sub(4,5)
print("Sum = ",result1)
print("difference = ",result2)
