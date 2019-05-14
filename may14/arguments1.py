#ARGUMENTS

def person(name,age):
    print("name= ",name)
    print("age= ",age)
    print(20*"__")

#positional
person("Ramesh",25)

#keyword
person(age=26,name="Suresh")

#******************************************
#DEFAULT ARGUMTS
def personDef(name="defalut",age=20):
    print("name= ",name)
    print("age= ",age)
    print(20*"__")
personDef("mathew",33)
personDef(25)
personDef(age=25)
personDef("Ganesh")
