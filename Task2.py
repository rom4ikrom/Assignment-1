#This is a simple program that allows user calculate an area and a length of a circle.
import math
radius = float(input("Radius:"))
area = math.pi * math.pow(radius, 2)
length = 2 * math.pi * radius
print("\nArea is: \t", area)
print("\nLength is: \t", length)
