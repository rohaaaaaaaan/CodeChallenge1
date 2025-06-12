import turtle  # Import the turtle graphics module

# Function to draw a square with a given side length
def square(t, length):
    for _ in range(4):  # A square has 4 sides
        t.forward(length)  # Move forward by the specified length
        t.right(90)         # Turn right by 90 degrees

# Set up the screen and the turtle
screen = turtle.Screen()   # Create a screen to display the turtle graphics
screen.bgcolor("white")    # Optional: Set the background color

bob = turtle.Turtle()      # Create a turtle named bob
bob.shape("turtle")        # Optional: Set the turtle shape to "turtle"
bob.color("blue")          # Optional: Set the turtle color to blue

# Test the square function with different lengths
square(bob, 100)  # First test with a side length of 100
square(bob, 50)   # Second test with a side length of 50
square(bob, 150)  # Third test with a side length of 150

# Hide the turtle after drawing
bob.hideturtle()

# Keep the window open until the user clicks on it
screen.exitonclick()
