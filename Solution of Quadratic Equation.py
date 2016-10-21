print (" This program can solve quadratic equations like a(x^2) + bx + c = 0 \n")
import math
# Here user enter the variable value of a, b, c
a = float(input(" Enter a "))
b = float(input(" Enter b "))
c = float(input(" Enter c "))
D = math.pow(b,2) - 4 * a * c 
float(D)
if D > 0:
    print (" \n Discriminant is ", D)
    print (" Square root of Discriminant is \n", math.sqrt(D))
    x1 = (-b + math.sqrt(D)) / (2 * a)
    print (" x1 is", x1)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print (" x2 is", x2)
elif D == 0:
    print (" \n Discriminant is \n", D)
    x = (-b) / (2 * a)
    print (" x is ", x)
else:
    print (" \n Discriminant is below 0 ")
    print (" The equation has no roots ")
print (" \n Thank you for using this program. ")
input()
