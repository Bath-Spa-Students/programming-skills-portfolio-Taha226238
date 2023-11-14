while True:
    age = input("what is your age?" )
    
    age = int(age)
    if age < 3:
        print("the ticket is free")
    elif age < 12:
        print("the ticket is $10") 
    else:
        print("the ticket is $15")