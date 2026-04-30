def exception9(a):
    for x in a:
        if a.count(x) == 1:
            return x
print (exception9([4,4,5,4,4,4,4,4,4]))