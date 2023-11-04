# Create a list of sandwich orders
<<<<<<< HEAD
<<<<<<< HEAD
sandwich_orders = ["tuna", "turkey", "club", "pastrami", "veggie"]
=======
sandwich_orders = ["turkey sandwich", "ham and cheese sandwich", "veggie sandwich", "tuna sandwich", "pastrami sandwich", "chicken sandwich", "BLT sandwich", "roast beef sandwich", "pastrami sandwich"]
>>>>>>> a647256d6b4e38deb229fb3ad9b91c786b2b6d31
=======
sandwich_orders = ["turkey sandwich", "ham and cheese sandwich", "veggie sandwich", "tuna sandwich", "pastrami sandwich", "chicken sandwich", "BLT sandwich", "roast beef sandwich", "pastrami sandwich"]
>>>>>>> a647256d6b4e38deb229fb3ad9b91c786b2b6d31

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Process the sandwich orders
while sandwich_orders:
<<<<<<< HEAD
<<<<<<< HEAD
    current_order = sandwich_orders.pop(0)
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

# Print the list of finished sandwiches
=======
=======
>>>>>>> a647256d6b4e38deb229fb3ad9b91c786b2b6d31
    current_order = sandwich_orders.pop()
    
    if current_order == "pastrami sandwich":
        print(f"Sorry, we're out of pastrami.")
    else:
        print(f"I made your {current_order}.")
        finished_sandwiches.append(current_order)

# Print a message listing each sandwich that was made
<<<<<<< HEAD
>>>>>>> a647256d6b4e38deb229fb3ad9b91c786b2b6d31
=======
>>>>>>> a647256d6b4e38deb229fb3ad9b91c786b2b6d31
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
