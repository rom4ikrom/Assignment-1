print (" This program can solve quadratic equations like a(x^2) + bx + c = 0 ")
print()
# Here user enter the variable value of a, b, c
a = float(input(" Enter a "))
b = float(input(" Enter b "))
c = float(input(" Enter c "))
print()
D = b * b - 4 * a * c 
float(D)
if D > 0:
    print (" Discriminant is ", D)
    print (" Square root of Discriminant is", D ** 0.5)
    print()
    x1 = (-b + D ** 0.5) / (2 * a)
    print (" x1 is", x1)
    x2 = (-b - D ** 0.5) / (2 * a)
    print (" x2 is", x2)
elif D == 0:
    print (" Discriminant is ", D)
    print ()
    x = (-b) / (2 * a)
    print (" x is ", x)
elif D < 0:
    print (" Discriminant is below 0 ")
    print (" The equation has no roots ")
print ()
print (" Thank you for using this program. ")
input()
