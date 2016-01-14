list = [45, 23, 12, 23, 12, 87, 23, 13, 75]
print(list)
print("length of list =", len(list))
x = 12
print(x, "in table", x in list)
index = 1
list.insert(index, x)
print("insert", x, "to", index)
print(list)
