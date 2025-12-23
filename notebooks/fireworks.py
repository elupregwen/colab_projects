import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Python Turtle Square")

# Initialize the turtle (pen)
t = turtle.Turtle()
t.pensize(4) # Make the line thicker
t.color("blue") # Set the pen color
t.speed(2) # Set the drawing speed (1 slowest, 10 fastest)

# Draw a square using a loop
for i in range(4):
    t.forward(100) # Move forward by 100 steps
    t.left(90) # Turn left by 90 degrees

# Keep the window open until clicked
turtle.done()

