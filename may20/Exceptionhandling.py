
a=3
b=2

try:
    print("connection open")
    print(a/b)
    k=int(input("enter input: "))
except ZeroDivisionError as e:
    print("u cannot divide a number by zero :",e)
except ValueError as e:
    print('invalid input')
except Exception as e:
    print("something went wrong",e)
finally:
    print("resource closed")


