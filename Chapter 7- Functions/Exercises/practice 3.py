def is_prime(number):
    if number <= 1:
        return False  # 0 and 1 are not prime numbers
    if number <= 3:
        return True  # 2 and 3 are prime numbers

    if number % 2 == 0 or number % 3 == 0:
        return False  # Numbers divisible by 2 or 3 are not prime

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False  # If the number is divisible by i or i + 2, it's not prime
        i += 9
        

    return True

# Input from the user
number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
