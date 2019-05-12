#lambda expression filter
nums=[1,2,5,4,77,55,7,88,9,44]
print("nums= ",nums)

def eve(n):
    return n%2==0
evensfun=list(filter(eve,nums))
print("evens using function= ",evensfun)



evens=list(filter(lambda n : n%2==0,nums))
print("evens using lambda= ",evens)

#MAP
doubles=list(map(lambda n : n*2,evens))
print("doubles= ",doubles)

#REDUCE
from functools import reduce 
sum= reduce(lambda a,b: a+b ,doubles)
print("sums= ", sum)



