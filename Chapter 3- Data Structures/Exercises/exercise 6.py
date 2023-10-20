# Create a list of people to invite to dinner
guests = ["mary", "rafia", "iftikar"]

# Print initial invitations to each person
for guest in guests:
    invitation = f"Dear {guest}, I would like to invite you to dinner. Please join me for a wonderful evening."
    print(invitation)

# Message indicating the limited space
print("\nI can only invite two people for dinner.\n")

# Remove guests using pop() and apologize
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

# Print invitations to the two remaining guests
for guest in guests:
    invitation = f"Dear {guest}, you're still invited to dinner."
    print(invitation)

# Use del to remove the last two names
del guests[:]
print("\nGuest list after removing the last two names:", guests)
