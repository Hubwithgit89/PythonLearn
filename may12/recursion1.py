#Recusion basic 1
i=1
def disp():
#issue about variable i
    global i
    print("Welcome",i)
    i+=1;
    disp()
disp()



