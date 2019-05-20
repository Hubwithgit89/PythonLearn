
def topTen():
    #instead of returb use yield
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

val=topTen()

print(val)
print(val.__next__())
#print(next(val))
print(val.__next__())
print(val.__next__())
print(val.__next__())
print(val.__next__())
#print(val.__next__())