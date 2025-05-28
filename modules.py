#modules - file containing code u wanna import into yr prg
#we use import statement to unclude the module (built in or your own)
#useful to break up a large prg into reusable seperate files
import math
import math as m # alias for module
from math import pi

a, b, c, d, e = 1, 2, 3, 4, 5
print(math.pi)
print(pi)

print(math.e ** a)
print(math.e ** b)
print(math.e ** c)
print(math.e ** d)
print(math.e ** e)

def square(x):
    return x**2

def cube(x):
    return x**3

def circumference(radius):
    return 2*pi*radius

def area(radius):
    return pi * radius * 2

pi=3.14159