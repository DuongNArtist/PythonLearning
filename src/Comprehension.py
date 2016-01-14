m = [2, 5, 6, 7, 12]
result = [x + 2 for x in m]
print(result)

rows = 'ABCDEFGHI'
cols = '123456789'
squares = [r + c for r in rows for c in cols]
print(squares)

l = [x for x in 'abcdefghi' if x < 'e']
print(l)
