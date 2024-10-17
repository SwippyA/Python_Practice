def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32

# Taking temperature in Celsius as input from the user
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Print the result
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")
