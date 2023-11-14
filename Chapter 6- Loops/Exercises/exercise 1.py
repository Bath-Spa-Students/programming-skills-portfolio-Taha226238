# Initialize an empty list to store pizza toppings
pizza_toppings = []

while True:
    topping = input("Enter your favirote pizza topping (or 'sauce' to pepporni): ")
    
    if topping.lower() == 'sauce':
        break  # Exit the loop if 'sauce' is entered
    else:
        pizza_toppings.append(topping)

# Print the list of pizza toppings
print("Your pizza toppings are:", ", ".join(pizza_toppings))

