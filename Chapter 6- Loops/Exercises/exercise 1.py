while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    
    if topping.lower() == 'quit':
        print("Quitting the pizza topping selection process.")
        break
    else:
        print(f"I'll add {topping} to your pizza.")
