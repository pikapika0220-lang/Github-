def exception3(x,y,z):
    if x == y:
        return z
    elif x == z:
        return y
    elif y == z:
        return x

print (exception3(5,2,5))