def handle_collision(list1):
    dic1 = {}
    for value in list1:
        dic1[value] = list1.index(value)
    return dic1

print (handle_collision(['hayate', 'kotaro-', 'morioka']))