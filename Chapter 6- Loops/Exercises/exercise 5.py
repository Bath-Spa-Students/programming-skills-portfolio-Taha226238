# Create a list of sandwich orders with pastrami
sandwich_orders = ["pastrami", "tuna", "pastrami", "turkey", "club", "pastrami", "ham and cheese", "vegetarian"]

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Print a message about running out of pastrami
print("Sorry, we've run out of pastrami sandwiches.")

# Remove all occurrences of 'pastrami' from sandwich_orders
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

# Loop through the remaining sandwich orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)  # Get the first order from the list
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

# Print the list of finished sandwiches
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
