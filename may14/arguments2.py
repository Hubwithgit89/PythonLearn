#Variable length aguments
def sum(*b):
    c=0
    for i in b:
        c=c+i;
    print(c)
sum(2,3,4,5,6)
sum(22,3,3,4345,345,345,45,34)


#*******************************
lst=[2,3,45]
#sum(lst)
#sum(*lst)
