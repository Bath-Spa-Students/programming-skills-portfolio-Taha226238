import math  # Import the math module for the value of pi

def calculate_circle_area(radius):
    if radius < 0:
        return "Invalid radius (negative value)"
    else:
        return math.pi * (radius ** 2)

# Input from the user
radius = float(input("Enter the radius of the circle: "))

area = calculate_circle_area(radius)

if isinstance(area, str):
    print(area)
else:
    print(f"The area of the circle with radius {radius} is {area:.2f}")
