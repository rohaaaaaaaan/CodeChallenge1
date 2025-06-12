import turtle

# Function to draw a regular polygon with n sides and a given length
def polygon(t, length, n):
    # Calculate the exterior angle of the polygon
    angle = 360 / n
    
    for _ in range(n):  # Draw n sides
        t.forward(length)  # Move forward by the length of each side
        t.left(angle)       # Turn left by the exterior angle

# Function to approximate an arc of a circle with a turtle and a given radius and angle
def arc(t, r, angle):
    # Approximate the arc by drawing a polygon with many sides
    # The number of sides (n) is typically chosen large enough to make the polygon appear circular.
    n = 360  # Number of sides (you can adjust this for better approximation)
    length = 2 * 3.14159 * r / n  # Calculate the length of each side
    
    # Calculate the number of sides to draw based on the given angle
    sides_to_draw = int(n * (angle / 360))  # Determine how many sides to draw for the angle
    
    for _ in range(sides_to_draw):  # Draw only the specified fraction of the circle
        t.forward(length)  # Move forward by the length of each side
        t.left(360 / n)     # Turn left by the exterior angle

# Create a turtle named 'bob'
bob = turtle.Turtle()

# Test the arc function with different radii and angles
radii_angles = [(50, 90), (100, 180), (150, 45), (200, 270)]  # List of (radius, angle) pairs to test

for r, angle in radii_angles:
    bob.penup()  # Lift the pen to move without drawing
    bob.goto(0, -r)  # Move the turtle to the starting position
    bob.pendown()  # Lower the pen to start drawing
    arc(bob, r, angle)  # Draw the arc
    bob.penup()  # Lift the pen after drawing

# Finish the turtle graphics
turtle.done()
