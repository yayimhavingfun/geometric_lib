import math


# accepts arguments a, b, c - sides, returns perimeter of a triangle
def perimeter(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return "values cannot be 0"
    if a + b >= c:
        return "side c should be less than the sum of the other two sides."
    if b + c >= a:
        return "side a should be less than the sum of the other two sides."
    if c + a >= b:
        return "side b should be less than the sum of the other two sides."

    return a + b + c


# accepts arguments a - side, h - height, returns area of a triangle
def area(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return "values cannot be 0"
    if a + b >= c:
        return "side c should be less than the sum of the other two sides."
    if b + c >= a:
        return "side a should be less than the sum of the other two sides."
    if c + a >= b:
        return "side b should be less than the sum of the other two sides."

    p = perimeter(a, b, c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
