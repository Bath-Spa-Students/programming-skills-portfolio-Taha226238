list1 = [5, 10, 15, 20, 25, 50, 20]
value_to_find = 20
replacement_value = 200
found = False

for i in range(len(list1)):
    if list1[i] == value_to_find:
        list1[i] = replacement_value
        found = True
        break

if found:
    print("Value 20 has replaced with 200:")
else:
    print("Value 20 is not found in the list.")

print(list1)
