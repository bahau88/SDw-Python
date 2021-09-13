import functools
from math import sqrt
from Task_1 import decorator_1
from Task_2 import decorator_2
from Task_3 import decorator_3
from Task_4 import decorator_4


@decorator_1
#Solve quadratic equation
def Equation(a,b,c):
    r = b ** 2 - 4 * a * c
    if r > 0:
        num_roots = 2
        x1 = (((-b) + sqrt(r)) / (2 * a))
        x2 = (((-b) - sqrt(r)) / (2 * a))
        print("There are 2 roots: %f and %f" % (x1, x2))
    elif r == 0:
        num_roots = 1
        x = (-b) / 2 * a
        print("There is one root: ", x)
    else:
        num_roots = 0
        print("No roots, discriminant < 0.")

Equation(1,4,4)

@decorator_2
# Print Pascal's Triangle in Python
def PascalTriangle(n):
   trow = [1]
   y = [0]
   for x in range(n):
      print(trow)
      trow=[left+right for left,right in zip(trow+y, y+trow)]
   return n>=1
