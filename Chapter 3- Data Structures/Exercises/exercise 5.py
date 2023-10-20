# Create a list of people to invite to dinner
guests = ["mary", "rafia", "iftikar"]

# Print initial invitations to each person
for guest in guests:
    invitation = f"Dear {guest}, I would like to invite you to dinner. Please join me for a wonderful evening."
    print(invitation)

# Name of the guest who can't make it
guest_cant_make_it = "mary"
print(f"\nUnfortunately, {guest_cant_make_it} can't make it to the dinner.\n")

# Replace the guest who can't make it with a new guest
new_guest = "nasir"
guests[guests.index(guest_cant_make_it)] = new_guest

# Print a second set of invitations
for guest in guests:
    invitation = f"Dear {guest}, I would like to invite you to dinner. Please join me for a wonderful evening."
    print(invitation)
