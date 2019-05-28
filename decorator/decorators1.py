#decorators,also called metaprogramming as a part of the program
#tries to modify another part of the program at compile time
def first(msg):
    print(msg)    

first("Hello")

second = first
second("Hello")
