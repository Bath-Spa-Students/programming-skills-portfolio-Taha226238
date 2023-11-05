while True:
    age_input = input("Please enter your age (or 'quit' to exit): ")
    
    if age_input.lower() == 'quit':
        break  # Exit the loop if the user enters 'quit'
    
    try:
        age = int(age_input)
        if age < 3:
            ticket_price = 0
        elif 3 <= age <= 12:
            ticket_price = 10
        else:
            ticket_price = 15
        
        print(f"Your ticket price is ${ticket_price}")
    except ValueError:
        print("Please enter a valid age as a number.")
