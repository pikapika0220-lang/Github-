def sum_list(ln):
    int = 0
    for x in ln:
        int = int + x
    return int

print(sum_list([10, 20, 30]) == 60)
print(sum_list([-1, 2, -3, 4, -5]) == -3)