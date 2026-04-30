def reverse_totuple(ln):
    ln.reverse()
    return tuple(ln)

print(reverse_totuple([1, 2, 3, 4, 5]) == (5, 4, 3, 2, 1))