my_information = {
    "first_name": "taha",
    "last_name": "khan",
    "age": 18,
    "gender": "Male",
    "location": "Ajman,UAE",
    "occupation": "Creative Computing",
    "hobbies": ["sports,read book,hangout with friend"],
    "favorite_food": "Pizza",
    "email": "taha@gmail.com",
}

# Accessing and printing information from the dictionary
print("First Name:", my_information["first_name"])
print("Last Name:", my_information["last_name"])
print("Age:", my_information["age"])
print("Gender:", my_information["gender"])
print("Location:", my_information["location"])
print("Occupation:", my_information["occupation"])
print("Hobbies:", ", ".join(my_information["hobbies"]))
print("Favorite Food:", my_information["favorite_food"])
print("Email:", my_information["email"])
