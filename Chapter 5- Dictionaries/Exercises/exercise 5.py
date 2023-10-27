# Create a list of dictionaries representing different pets
pets = [
    {'kind': 'Dog', 'owner': 'Alice'},
    {'kind': 'Cat', 'owner': 'Bob'},
    {'kind': 'Fish', 'owner': 'Charlie'},
    {'kind': 'Bird', 'owner': 'David'},
    {'kind': 'Rabbit', 'owner': 'Eve'}
]

# Loop through the list and print information about each pet
for pet in pets:
    print(f"Kind of Animal: {pet['kind']}")
    print(f"Owner's Name: {pet['owner']}")
    print()
