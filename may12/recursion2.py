#Recusion basic 2
import sys
print("before  = ",sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print("after  = ",sys.getrecursionlimit())
i=1
def disp():
    global i
    print("Welcome",i)
    i+=1;
    #disp()
disp()



