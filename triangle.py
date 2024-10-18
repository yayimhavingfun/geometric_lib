import math

#accepts arguments a, b, c - sides, returns perimeter of a triangle
def perimeter(a, b, c):
    return a + b + c
#accepts arguments a - side, h - height, returns area of a triangle
def area(a, b, c):
    p = perimeter(a, b, c) / 2
    return math.sqrt(p * (p-a) * (p-b) * (p-c))`


