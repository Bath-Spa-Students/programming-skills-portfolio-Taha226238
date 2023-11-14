target_value = 10

for number in range(1, 11):
    if number == target_value:
        print(f"Found the target value: {target_value}")
        break  # Exit the loop when the condition is met
    else:
        print(f"the number is: {number}")
