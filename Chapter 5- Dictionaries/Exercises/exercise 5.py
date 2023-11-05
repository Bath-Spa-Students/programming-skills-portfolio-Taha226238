# Create a list of dictionaries representing different pets
pets = [
    {'kind': 'Dog', 'owner': 'taha'},
    {'kind': 'Cat', 'owner': 'irtaza'},
    {'kind': 'Fish', 'owner': 'abdu'},
    {'kind': 'Bird', 'owner': 'faseeh'},
    {'kind': 'Rabbit', 'owner': 'kamran'}
]

# Loop through the list and print information about each pet
for pet in pets:
    print(f"Kind of Animal: {pet['kind']}")
    print(f"Owner's Name: {pet['owner']}")
    print()
