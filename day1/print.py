name = "Jack"
print(name)

name = "Angela"
print(name)

# print(len(input("What is your name?")))

username=input("What is your name?")
lenght=len(username)
print("Number of characters: ",lenght)

# Create a greeting for your program.
# Ask the user for the city that they grew up in and store it in a variable.
# Ask the user for the name of a pet and store it in a variable.
# Combine the name of their city and pet and show them their band name.

print("Band Name Generator project ")
cityName = input("Which city did you grow up in\n?")
petName = input("What is the name of a pet\n?")
print("Your band name could be " + cityName + " " + petName)
