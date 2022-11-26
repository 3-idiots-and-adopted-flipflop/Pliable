# ax^2 + bx  + c

import math

a = int(input("Enter 1st value: "))
b = int(input("Enter 2nd value: "))
c = int(input("Enter 3rd value: "))

# x= (-b +/- sqrt(b^2 - 4*a*c)) /2a
# d= b^2 - 4*a*c

d = (b**2 - (4*a*c))

if (d>0):
    x1= ((-1 * b) + math.sqrt(d)) / (2*a)
    x2= ((-1 * b) - math.sqrt(d)) / (2*a)
    print("The 2 values of x are: ",x1, "and", x2)

elif (d==0):
    x= ((-1 * b) + math.sqrt(d)) / (2*a)
    print("The value of x is: ",x)

else: 
    print("The equation has no real roots")
