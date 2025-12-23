import turtle
import random
import time
import math

# ---------------- SCREEN ----------------
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")
screen.title("🎆 Superb Fireworks Show 🎆")
screen.tracer(0)

# ---------------- TURTLES ----------------
rocket = turtle.Turtle(visible=False)
rocket.speed(0)
rocket.width(3)

particle = turtle.Turtle(visible=False)
particle.speed(0)
particle.width(2)

spark = turtle.Turtle(visible=False)
spark.speed(0)
spark.width(1)

# ---------------- COLORS ----------------
colors = [
    "#ff4d4d", "#ff9933", "#ffff66",
    "#66ff66", "#66ccff", "#9966ff",
    "#ff66cc", "white"
]

# ---------------- ROCKET LAUNCH ----------------
def launch_rocket(x):
    rocket.clear()
    rocket.penup()
    rocket.goto(x, -350)
    rocket.setheading(90)
    rocket.color("white")
    rocket.pendown()

    peak = random.randint(120, 280)

    for _ in range(35):
        rocket.forward(12)
        # glowing trail
        rocket.dot(4, "white")
        screen.update()
        time.sleep(0.015)

    rocket.clear()
    return rocket.xcor(), rocket.ycor()

# ---------------- EXPLOSION ----------------
def explode(x, y):
    particle.clear()
    spark.clear()

    burst_color = random.choice(colors)
    particle.color(burst_color)
    spark.color("white")

    particles = random.randint(35, 55)
    angles = [random.uniform(0, 360) for _ in range(particles)]
    speeds = [random.uniform(4, 8) for _ in range(particles)]
    gravity = 0.15

    positions = [(x, y)] * particles

    for frame in range(35):
        particle.clear()
        spark.clear()

        for i in range(particles):
            angle = math.radians(angles[i])
            vx = speeds[i] * math.cos(angle)
            vy = speeds[i] * math.sin(angle) - gravity * frame

            px = positions[i][0] + vx
            py = positions[i][1] + vy
            positions[i] = (px, py)

            # explosion particles
            particle.penup()
            particle.goto(px, py)
            particle.dot(5)

            # sparkle effect
            if random.random() > 0.7:
                spark.penup()
                spark.goto(px + random.randint(-2, 2), py)
                spark.dot(3)

        screen.update()
        time.sleep(0.03)

# ---------------- FIREWORK ----------------
def firework():
    x = random.randint(-450, 450)
    ex, ey = launch_rocket(x)
    explode(ex, ey)

# ---------------- SHOW ----------------
for _ in range(18):
    # sometimes launch double rockets
    if random.random() > 0.7:
        firework()
        firework()
    else:
        firework()

    time.sleep(random.uniform(0.2, 0.5))

turtle.done()
