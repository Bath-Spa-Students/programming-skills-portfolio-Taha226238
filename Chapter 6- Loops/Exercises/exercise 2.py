while True:
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
>>>>>>> a647256d6b4e38deb229fb3ad9b91c786b2b6d31
    age_str = input("Please enter your age (or 'quit' to exit): ")

    if age_str.lower() == 'quit':
        break

    try:
        age = int(age_str)

        if age < 3:
            print("Your ticket is free.")
        elif 3 <= age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")
<<<<<<< HEAD
>>>>>>> a647256d6b4e38deb229fb3ad9b91c786b2b6d31
=======
>>>>>>> a647256d6b4e38deb229fb3ad9b91c786b2b6d31
    except ValueError:
        print("Please enter a valid age as a number.")
