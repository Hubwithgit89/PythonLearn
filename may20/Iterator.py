#Iterator

class TopTen:

    def __init__(self):
        self.num=1


    def __iter__(self):
        return  self

    def __next__(self):
        if self.num <=10:
            val=self.num
            self.num +=1
            return val
        else:
            #reason fol else to raise exception to stop for loop
            #try without else

            raise StopIteration

t=TopTen()

#output if belowline is uncommented
#print(next(t))

for i in t:
    print(i)
