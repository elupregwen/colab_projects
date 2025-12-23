import turtle
import random
import math

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fireworks Display 🎆")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off animation for instant drawing

# Create turtle for drawing
fireworks = []
particles = []

# Function to create a firework
def create_firework(x, y):
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "magenta"]
    color = random.choice(colors)
    
    # Create firework shell
    shell = turtle.Turtle()
    shell.hideturtle()
    shell.color(color)
    shell.penup()
    shell.goto(0, -250)  # Start from bottom
    shell.showturtle()
    shell.shape("circle")
    shell.shapesize(0.3)
    shell.speed(0)
    
    # Calculate trajectory
    angle = random.uniform(60, 120)  # 60-120 degrees
    power = random.uniform(8, 12)
    
    fireworks.append({
        "turtle": shell,
        "x": 0,
        "y": -250,
        "vx": math.cos(math.radians(angle)) * power,
        "vy": math.sin(math.radians(angle)) * power,
        "color": color,
        "target_x": x,
        "target_y": y,
        "exploded": False,
        "gravity": 0.15
    })

# Function to explode firework
def explode_firework(firework):
    x, y = firework["turtle"].pos()
    color = firework["color"]
    
    # Create explosion particles
    for _ in range(random.randint(30, 50)):
        particle = turtle.Turtle()
        particle.hideturtle()
        particle.color(color)
        particle.penup()
        particle.goto(x, y)
        particle.showturtle()
        particle.shape("circle")
        particle.shapesize(0.15)
        
        # Random direction and speed
        angle = random.uniform(0, 360)
        speed = random.uniform(2, 6)
        
        particles.append({
            "turtle": particle,
            "x": x,
            "y": y,
            "vx": math.cos(math.radians(angle)) * speed,
            "vy": math.sin(math.radians(angle)) * speed,
            "color": color,
            "life": random.randint(40, 80),
            "gravity": 0.1,
            "fade": random.uniform(0.9, 0.97)
        })
    
    # Remove the firework shell
    firework["turtle"].hideturtle()

# Update function for animation
def update():
    global fireworks, particles
    
    # Update fireworks
    for firework in fireworks[:]:
        if not firework["exploded"]:
            # Update position
            firework["x"] += firework["vx"]
            firework["y"] += firework["vy"]
            firework["vy"] -= firework["gravity"]
            
            firework["turtle"].goto(firework["x"], firework["y"])
            
            # Check if it should explode
            if firework["vy"] < 0:  # Reached peak
                distance_to_target = math.sqrt(
                    (firework["x"] - firework["target_x"])**2 + 
                    (firework["y"] - firework["target_y"])**2
                )
                
                if distance_to_target < 50 or firework["vy"] < -2:
                    explode_firework(firework)
                    firework["exploded"] = True
                    fireworks.remove(firework)
    
    # Update particles
    for particle in particles[:]:
        particle["x"] += particle["vx"]
        particle["y"] += particle["vy"]
        particle["vy"] -= particle["gravity"]
        particle["life"] -= 1
        
        # Apply fading effect
        current_size = particle["turtle"].shapesize()[0]
        particle["turtle"].shapesize(current_size * particle["fade"])
        
        # Update particle position
        particle["turtle"].goto(particle["x"], particle["y"])
        
        # Remove dead particles
        if particle["life"] <= 0 or particle["y"] < -300:
            particle["turtle"].hideturtle()
            particles.remove(particle)
    
    # Randomly create new fireworks
    if random.random() < 0.05 and len(fireworks) < 3:
        create_firework(
            random.randint(-300, 300),
            random.randint(100, 250)
        )
    
    screen.update()
    screen.ontimer(update, 30)  # 30ms delay = ~33 FPS

# Mouse click to launch firework
def launch_firework(x, y):
    create_firework(x, y)

# Add click event
screen.onclick(launch_firework)

# Create initial fireworks
for _ in range(2):
    create_firework(
        random.randint(-300, 300),
        random.randint(100, 250)
    )

# Start animation
update()

# Add instructions text
instructions = turtle.Turtle()
instructions.hideturtle()
instructions.color("white")
instructions.penup()
instructions.goto(0, -280)
instructions.write("Click anywhere to launch fireworks! 🎆", align="center", font=("Arial", 12, "normal"))

# Add title
title = turtle.Turtle()
title.hideturtle()
title.color("white")
title.penup()
title.goto(0, 260)
title.write("PYTHON FIREWORKS DISPLAY", align="center", font=("Arial", 20, "bold"))

print("🎆 Fireworks simulation started!")
print("🎯 Click on the black screen to launch fireworks!")
print("🖱️ Close the window to exit.")

# Keep window open
screen.mainloop()