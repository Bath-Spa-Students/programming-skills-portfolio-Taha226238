# Create a list of sandwich orders
sandwich_orders = ["sausage", "zinger", "vegetarian", "tandoori", "chicken cheese", "chicken"]

# Create an empty list for finished sandwiches
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    
    if current_order == "chicken cheese":
        print(f"Sorry, we're out of {current_order} right now.")
    else:
        print(f"I made your {current_order} sandwich.")
        finished_sandwiches.append(current_order)

print("\nFinished Sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
