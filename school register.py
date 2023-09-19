# Initialize an empty School Register
school_register = []

# Continuously add values to the list until the user decides to stop
while True:
    name = input("Enter a name (or 'stop' to quit): ")
    
    # Check if the user wants to stop
    if name.lower() == 'stop':
        break
    
    # Add the entered value to the list
    school_register.append(name)

# Print the final list
print("Updated School Register:", school_register)
