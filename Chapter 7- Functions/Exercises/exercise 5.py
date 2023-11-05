def describe_city(city, country="UAE"):
    print(f"{city} is in {country}.")

# Call the function for three different cities, including one not in the default country
describe_city("Ajman")
describe_city("Dubai", "UAE")
describe_city("AL AIN", "UAE")
