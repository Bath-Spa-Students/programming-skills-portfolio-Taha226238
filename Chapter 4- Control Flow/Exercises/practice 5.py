# Get the month as input from the user
month = input("Enter a month (e.g., January, February, etc.): ")

# Convert the input to lowercase to handle case-insensitivity
month = month.lower()

# Check the month to determine the season
if month in ("december", "january", "february"):
    season = "Winter"
elif month in ("march", "april", "may"):
    season = "Spring"
elif month in ("june", "july", "august"):
    season = "Summer"
elif month in ("september", "october", "november"):
    season = "Autumn (Fall)"
else:
    season = "Invalid Month"

print(f"The season for {month.capitalize()} is {season}.")
