n=int(input("enter the value of n:"))
d=int(input("enter the value of d:"))
c=int(input("enter the value of c:"))
try:
    q=n/(d-c)
    print("quotient:",q)
except ZeroDivisionError:
    print("division by zero!")




output:
    enter the value of n:10
    enter the value of d:5
    enter the value of c:5
    division by zero!
