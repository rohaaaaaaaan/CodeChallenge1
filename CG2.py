def right_justify(s):
    # Calculate how many spaces are needed to make the string's last character in column 70
    spaces_needed = 70 - len(s)
    
    # Print the string with the calculated number of leading spaces
    print(' ' * spaces_needed + s)

# Test the function
right_justify('allen')
