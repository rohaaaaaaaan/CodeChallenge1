def is_triangle(a, b, c):
    # Check if any side is greater than the sum of the other two
    if a + b > c and a + c > b and b + c > a:
        print("Yes")
    else:
        print("No")

def main():
    # Prompt the user for three stick lengths
    a = int(input("Enter the first stick length: "))
    b = int(input("Enter the second stick length: "))
    c = int(input("Enter the third stick length: "))
    
    # Use the is_triangle function to check if the sticks can form a triangle
    is_triangle(a, b, c)

# Call the main function
main()
