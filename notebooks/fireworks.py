import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("🎆 Realistic Fireworks Show 🎆")
screen.tracer(0)

# Rocket turtle
rocket = turtle.Turtle()
rocket.hideturtle()
rocket.speed(0)
rocket.width(3)

# Explosion turtle
boom = turtle.Turtle()
boom.hideturtle()
boom.speed(0)
boom.width(2)

colors = [
    "#ff4d4d", "#ff9933", "#ffff66",
    "#66ff66", "#66ccff", "#9966ff",
    "#ff66cc", "white"
]

def launch_rocket(x):
    rocket.color("white")
    rocket.penup()
    rocket.goto(x, -300)
    rocket.setheading(90)
    rocket.pendown()

    peak = random.randint(50, 250)

    for _ in range(30):
        rocket.forward(10)
        screen.update()
        time.sleep(0.02)

    rocket.clear()
    return rocket.xcor(), rocket.ycor()

def explode(x, y):
    boom.penup()
    boom.goto(x, y)
    boom.pendown()

    color = random.choice(colors)
    boom.color(color)

    particles = random.randint(25, 40)

    for _ in range(particles):
        boom.penup()
        boom.goto(x, y)
        boom.setheading(random.randint(0, 360))
        boom.pendown()
        boom.forward(random.randint(60, 120))

    screen.update()
    time.sleep(0.5)
    boom.clear()

def firework():
    x = random.randint(-300, 300)
    ex, ey = launch_rocket(x)
    explode(ex, ey)

# Fireworks show
for _ in range(15):
    firework()
    time.sleep(0.3)

turtle.done()
