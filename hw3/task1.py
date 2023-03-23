list = [15, 6, 5, 3, 12, 14, 11, 9, 17, 4, 17, 5]

duplicates = [x for i, x in enumerate(list) if i != list.index(x)]
print(duplicates)
