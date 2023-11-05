while True:
    age = input("How old are you?" )
    
    age = int(age)
    if age < 3:
        print("your ticket is free")
    elif age < 12:
        print("your ticket is $10") 
    else:
        print("your ticket is $15")