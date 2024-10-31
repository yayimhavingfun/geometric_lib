import math


# accepts r - radius, returns area of a circle
def area(r):
    if r == 0:
        return "r cannot be 0"
    return math.pi * r * r


# accepts r - radius, returns perimeter of a circle
def perimeter(r):
    if r == 0:
        return "r cannot be 0"
    return 2 * math.pi * r
