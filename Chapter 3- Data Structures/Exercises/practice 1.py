list1 = [5, 20, 15, 20, 25, 50, 20]
item_to_remove = 20

list1 = [x for x in list1 if x != item_to_remove]

print(list1)
