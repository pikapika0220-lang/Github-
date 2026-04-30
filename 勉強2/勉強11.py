def atgc_countlist(str_atgc):
    list_count = []
    for bp in 'ATGC':
        list_count.append([str_atgc.count(bp),bp])
    return list_count 
print(atgc_countlist('AAGCCCCATGGTAA'))