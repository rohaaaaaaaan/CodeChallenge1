import turtle

# Function to draw a regular polygon with n sides and a given length
def polygon(t, length, n):
    # Calculate the exterior angle of the polygon
    angle = 360 / n
    
    for _ in range(n):  # Draw n sides
        t.forward(length)  # Move forward by the length of each side
        t.left(angle)       # Turn left by the exterior angle

# Function to approximate a circle with a turtle and a given radius
def circle(t, r):
    # Approximate the circle by drawing a polygon with many sides
    # We choose a polygon with enough sides to approximate a circle.
    # The number of sides (n) is typically chosen large enough to make the polygon appear circular.
    n = 360  # Number of sides (you can adjust this for better approximation)
    length = 2 * 3.14159 * r / n  # Calculate the length of each side
    
    polygon(t, length, n)  # Call polygon function to draw the circle

# Create a turtle named 'bob'
bob = turtle.Turtle()

# Test the circle function with different radii
radii = [50, 100, 150, 200]  # List of different radii to test

for r in radii:
    bob.penup()  # Lift the pen to move without drawing
    bob.goto(0, -r)  # Move the turtle to the starting position
    bob.pendown()  # Lower the pen to start drawing
    circle(bob, r)  # Draw the circle
    bob.penup()  # Lift the pen after drawing

# Finish the turtle graphics
turtle.done()
