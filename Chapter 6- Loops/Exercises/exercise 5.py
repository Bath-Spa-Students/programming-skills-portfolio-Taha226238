# Create a list of sandwich orders with chicken cheese
sandwich_orders = ["chicken cheese", "tandoori", "tikka", "sausage", "club", "nuterella", " cheese", "vegetarian"]

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Print a message about running out of chicken cheese
print("Sorry, we've run out of chicken cheese sandwiches.")

# Remove all occurrences of 'chicken ' from sandwich_orders
while "chicken cheese" in sandwich_orders:
    sandwich_orders.remove("chicken cheese")

# Loop through the remaining sandwich orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)  # Get the first order from the list
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

# Print the list of finished sandwiches
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
