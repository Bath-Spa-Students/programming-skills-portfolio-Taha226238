def make_shirt(size="Large", message="I love Python"):
    print(f"Creating a shirt of size {size} with the message: '{message}'")

# Create a large shirt with the default message
make_shirt()

# Create a medium shirt with the default message
make_shirt(size="Medium")

# Create a shirt of any size with a different message
make_shirt(size="Small", message="Python is awesome!")
