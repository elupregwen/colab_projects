import turtle
import random
import math

# Set up the screen (larger window for bigger display)
screen = turtle.Screen()
screen.setup(width=1000, height=700)  # Bigger window for a grander show
screen.bgcolor("black")
screen.title("Fireworks Display - Enhanced Version")
screen.tracer(0)  # Turn off animation for smoother updates
turtle.colormode(255)  # Allow RGB values from 0-255

# Create a turtle for drawing
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# Particle class (bigger sizes, twinkling effect)
class Particle:
    def __init__(self, x, y, vx, vy, color, size, lifetime):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.size = size
        self.lifetime = lifetime
        self.age = 0
        self.twinkle = random.uniform(0.8, 1.2)  # For twinkling effect

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy -= 0.1  # Gravity (corrected to pull downward)
        self.age += 1
        # Shrink and twinkle
        self.size = max(1, self.size * (1 - self.age / self.lifetime) * self.twinkle)
        self.twinkle = random.uniform(0.8, 1.2)  # Random twinkle

    def draw(self):
        if self.age < self.lifetime:
            pen.penup()
            pen.goto(self.x, self.y)
            pen.dot(self.size, self.color)

# Smoke class (bigger, more lingering)
class Smoke:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-0.5, 0.5)  # Slow drift
        self.vy = random.uniform(-0.2, 0.2)
        self.size = random.randint(3, 8)  # Bigger smoke
        self.lifetime = random.randint(150, 300)  # Longer lasting
        self.age = 0
        self.color = (80, 80, 80)  # Darker gray smoke

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.age += 1
        self.size = max(1, self.size * (1 - self.age / self.lifetime))

    def draw(self):
        if self.age < self.lifetime:
            pen.penup()
            pen.goto(self.x, self.y)
            pen.dot(self.size, self.color)

# Rocket class (bigger, centered launches, corrected upward movement)
class Rocket:
    def __init__(self, x, y, target_y):
        self.x = x
        self.y = y
        self.target_y = target_y
        self.vy = 8  # Positive velocity for upward movement
        self.smoke_trail = []  # Enhanced smoke trail
        self.exploded = False

    def update(self):
        if not self.exploded:
            self.y += self.vy
            # Add more smoke particles to trail
            self.smoke_trail.append(Smoke(self.x, self.y))
            if len(self.smoke_trail) > 20:  # Longer trail
                self.smoke_trail.pop(0)
            if self.y >= self.target_y:  # Corrected condition for upward movement
                self.explode()

    def explode(self):
        self.exploded = True
        particles = []
        num_particles = random.randint(100, 200)  # Way more particles for epic bursts
        explosion_type = random.choice(["burst", "fountain", "star"])
        for _ in range(num_particles):
            if explosion_type == "burst":
                angle = random.uniform(0, 2 * math.pi)
                speed = random.uniform(2, 6)
            elif explosion_type == "fountain":
                angle = random.uniform(-math.pi/4, math.pi/4)  # Narrower upward
                speed = random.uniform(1, 5)
            else:  # Star
                angle = random.uniform(0, 2 * math.pi)
                speed = random.uniform(3, 8)  # Faster for starburst
            vx = speed * math.cos(angle)
            vy = speed * math.sin(angle)
            color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))  # Brighter colors
            size = random.randint(3, 10)  # Bigger particles
            lifetime = random.randint(80, 150)
            particles.append(Particle(self.x, self.y, vx, vy, color, size, lifetime))
        return particles

    def draw(self):
        if not self.exploded:
            pen.penup()
            pen.goto(self.x, self.y)
            pen.dot(8, "white")  # Bigger rocket head
            # Draw smoke trail
            for smoke in self.smoke_trail:
                smoke.update()
                smoke.draw()

# Main simulation
particles = []
rockets = []
smokes = []  # Global smoke list for lingering effects

def update():
    global particles, rockets, smokes
    
    # Clear screen
    pen.clear()
    
    # Launch new rockets frequently, centered in the window
    if random.random() < 0.2 and len(rockets) < 10:  # Even more frequent, more rockets
        # Centered launches: bias towards center (-100 to 100), but allow some spread
        x = random.randint(-150, 150)  # Tighter center for focus
        target_y = random.randint(50, 250)  # Higher bursts (adjusted for upward movement)
        rockets.append(Rocket(x, -350, target_y))  # Launch from lower bottom
    
    # Update rockets
    new_particles = []
    for rocket in rockets[:]:
        rocket.update()
        if rocket.exploded:
            new_particles.extend(rocket.explode())
            rockets.remove(rocket)
        else:
            rocket.draw()
    
    # Update particles
    particles.extend(new_particles)
    for particle in particles[:]:
        particle.update()
        if particle.age >= particle.lifetime:
            particles.remove(particle)
        else:
            particle.draw()
    
    # Update and draw lingering smokes
    smokes.extend([smoke for rocket in rockets for smoke in rocket.smoke_trail if smoke not in smokes])
    for smoke in smokes[:]:
        smoke.update()
        if smoke.age >= smoke.lifetime:
            smokes.remove(smoke)
        else:
            smoke.draw()
    
    screen.update()
    screen.ontimer(update, 40)  # Faster updates for smoother animation

# Start the simulation
update()

# Keep the window open
turtle.done()