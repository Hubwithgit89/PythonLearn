#VARIABLE ARGUMETS AS DICTIONARY
def person(name,**data):
    print(name)
    print(data)
    print("printig data key wise")
    for x,y in data.items():
        print(x,y,sep=" = ")
        
    print(20*"__")

person("ABC",age=35,city="chennai")

person("CDE",age=35,city="chennai",company="IVTL")
