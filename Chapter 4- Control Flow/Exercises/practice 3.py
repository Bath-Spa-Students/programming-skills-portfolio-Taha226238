# Assuming you have two variables, amount1 and amount2
amount1 = 15  # Replace with the actual value of amount1
amount2 = 75  # Replace with the actual value of amount2

if amount1 > 10:
    if amount2 < 100:
        if amount1 > amount2:
            print("The greater of the amount1 and amount2 is:", amount1)
        else:
            print("The greater of the amount1 and amount2 is:", amount2)
    else:
        print("amount2 is not less than 100.")
else:
    print("amount1 is not greater than 10.")
