# Define the person's name with whitespace at the beginning and end
name = "\t\n   John Doe   \t\n"

# Print the name once to display the whitespace around it
print("Original Name:", name)

# Print the name using each stripping function
print("Using lstrip():", name.lstrip())
print("Using rstrip():", name.rstrip())
print("Using strip():", name.strip())
