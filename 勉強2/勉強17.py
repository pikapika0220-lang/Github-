ppap = {'apple' : 3, 'pen' : 5}
print('キーappleに対応する値 = ', ppap.setdefault('apple',7))
print('setdefault("apple", 7)を実行後の辞書 = ', ppap)
print('キーorangeに対応する値 = ', ppap.setdefault('orange', 7))
print('setdefault("orange", 7)を実行後の辞書 = ', ppap)

print (list(ppap.keys()))
print (list(ppap.values()))