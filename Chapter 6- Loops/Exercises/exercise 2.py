while True:
    try:
        age = int(input("Please enter your age (or enter '0' to quit): "))
        
        if age == 0:
            print("Exiting the ticket pricing system.")
            break
        elif age < 3:
            ticket_price = 0
        elif age >= 3 and age <= 12:
            ticket_price = 10
        else:
            ticket_price = 15
        
        print(f"The cost of your movie ticket is ${ticket_price}")
    except ValueError:
        print("Please enter a valid age as a number.")
