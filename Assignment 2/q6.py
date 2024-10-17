def km_to_miles(km):
    return km * 0.621371

# Taking kilometers as input from the user
kilometers = float(input("Enter distance in kilometers: "))

# Convert to miles
miles = km_to_miles(kilometers)

# Print the result
print(f"{kilometers} kilometers is equal to {miles} miles")
