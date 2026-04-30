def sum_lists(list1):
    total = 0
    for list2 in list1:
        for i in range(len(list2)):
            total += list2[i]
    return total


print(sum_lists([[20, 5], [6, 16, 14, 5], [16, 8, 16, 17, 14], [1], [5, 3, 5, 7]]) == 158)

