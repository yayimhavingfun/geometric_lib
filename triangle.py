import math

# Checks if the three sides can form a valid triangle.
def is_valid(a, b, c):
    return a + b > c and a + c > b and b + c > a


# accepts arguments a, b, c - sides, returns perimeter of a triangle
def perimeter(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return "values cannot be 0"
    if not is_valid(a, b, c):
        return "the provided side lengths do not form a valid triangle"
    return a + b + c


# accepts arguments a - side, h - height, returns area of a triangle
def area(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return "values cannot be 0"
    if not is_valid(a, b, c):
        return "the provided side lengths do not form a valid triangle"

    p = perimeter(a, b, c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
