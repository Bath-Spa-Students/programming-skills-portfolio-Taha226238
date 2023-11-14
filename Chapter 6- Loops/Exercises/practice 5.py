largest = None  # Initialize the variable to store the largest number

while True:
    user_input = input("Enter your number (or 0 to exit): ")

    if user_input == '0':
        break  # Exit the loop if the user enters '0'

    try:
        number = int(user_input)  # Convert the user input to an integer
        if largest is None or number > largest:
            largest = number  # Update the largest number if needed
    except ValueError:
        print("Invalid input. Please enter a number or '0' to exit.")

if largest is not None:
    print(f"The biggest number you have entered is: {largest}")
else:
    print("the number is not valid.")
