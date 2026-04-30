import math
def qe_disc(a, b, c):
    return b**2-4*a*c

def qe_solution1(a, b, c):
    return (-b-math.sqrt(qe_disc(a, b, c)))/(2*a)

def qe_solution2(a, b, c):
    return (-b+math.sqrt(qe_disc(a, b, c)))/(2*a)

assert qe_disc(1, -2, 1) == 0
assert qe_disc(1, -5, 6) == 1
assert round(qe_solution1(1, -2, 1) - 1, 6) == 0
assert round(qe_solution2(1, -2, 1) - 1, 6) == 0
assert round(qe_solution1(1, -5, 6) - 2, 6) == 0
assert round(qe_solution2(1, -5, 6) - 3, 6) == 0
