def describe_city(city, country="USA"):
    print(f"{city} is in {country}.")

# Call the function for three different cities, including one not in the default country
describe_city("New York")
describe_city("Reykjavik", "Iceland")
describe_city("Paris", "France")
