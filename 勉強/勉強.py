def sum_list(ln):
    int_sum = 0
    for value in ln:
        int_sum += value
    return int_sum
    
print(sum_list([10, 20, 30]) == 60)
