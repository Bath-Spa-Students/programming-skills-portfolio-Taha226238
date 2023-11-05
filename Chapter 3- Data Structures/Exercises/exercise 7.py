# Create a list of places to visit
places_to_visit = ["karachi", "lahore", "islamabad", "balochistan", "kashmir"]

# Print the original list
print("Original List:", places_to_visit)

# Print the sorted list in alphabetical order without modifying the original list
print("Sorted List (Alphabetical):", sorted(places_to_visit))

# Verify that the original list is still in its original order
print("Original List:", places_to_visit)

# Print the sorted list in reverse alphabetical order without modifying the original list
print("Sorted List (Reverse Alphabetical):", sorted(places_to_visit, reverse=True))

# Verify that the original list is still in its original order
print("Original List:", places_to_visit)

# Use reverse() to change the order of the original list
places_to_visit.reverse()
print("Reversed List:", places_to_visit)

# Use reverse() again to change the order back to the original order
places_to_visit.reverse()
print("Reversed Back to Original Order:", places_to_visit)

# Use sort() to change the order of the list to alphabetical order
places_to_visit.sort()
print("Sorted Using sort() (Alphabetical):", places_to_visit)

# Use sort() to change the order of the list to reverse alphabetical order
places_to_visit.sort(reverse=True)
print("Sorted Using sort(reverse=True) (Reverse Alphabetical):", places_to_visit)
