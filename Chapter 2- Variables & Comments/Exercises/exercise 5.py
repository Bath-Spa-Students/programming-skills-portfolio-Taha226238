# Define the cost of one USB stick and the girl's budget
usb_stick_cost = 6  # cost of one USB stick in pounds
budget = 50  # girl's budget in pounds

# Calculate the maximum number of USB sticks she can buy
num_usb_sticks = budget // usb_stick_cost

# Calculate the remaining pounds after the purchase
remaining_pounds = budget % usb_stick_cost

# Display the results
print("The girl have  buy", num_usb_sticks, "USB sticks.")
print("She will have", remaining_pounds, "pounds left.")
