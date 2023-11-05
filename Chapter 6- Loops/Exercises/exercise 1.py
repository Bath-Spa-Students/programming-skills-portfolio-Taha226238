# Initialize an empty list to store pizza toppings
pizza_toppings = []

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    
    if topping.lower() == 'quit':
        break  # Exit the loop if 'quit' is entered
    else:
        pizza_toppings.append(topping)

# Print the list of pizza toppings
print("Your pizza toppings are:", ", ".join(pizza_toppings))

