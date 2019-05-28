#introduction to decorator with higher order function exaample

def hi(name):
    return 'Hi '+ name

def bye(name):
    return "bye "+ name

def say(fun,x):
    result=fun(x)
    print(result)