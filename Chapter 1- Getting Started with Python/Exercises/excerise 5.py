# Accept the radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle using the formula A = πr^2
pi = 3.14159  # Approximate value of pi
area = pi * (radius ** 2)

# Display the result
print(f"The area of the circle with radius {radius} is {area:.2f}")