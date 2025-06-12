import turtle

# Function to draw a regular polygon with n sides and a given length
def polygon(t, length, n):
    # Calculate the exterior angle of the polygon
    angle = 360 / n
    
    for _ in range(n):  # Draw n sides
        t.forward(length)  # Move forward by the length of each side
        t.left(angle)       # Turn left by the exterior angle

# Create a turtle named 'bob'
bob = turtle.Turtle()

# Call the polygon function with 'bob', a side length of 100, and a polygon with 6 sides (hexagon)
polygon(bob, 100, 6)  # You can test with different values for 'n'

# Finish the turtle graphics
turtle.done()
