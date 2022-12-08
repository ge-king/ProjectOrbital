import math
import pygame

G = 6.67408e-11  # gravitational constant
M = 5.972e24  # mass of the Earth
R = 6371e3  # radius of the Earth

# Define the initial state of the spacecraft
x0 = R + 500e3  # initial x position (500 km above the surface of the Earth)
y0 = 0  # initial y position (on the equator)
vx0 = 0  # initial x velocity (not moving initially)
vy0 = 7.7e3  # initial y velocity (orbiting speed at 500 km altitude)

# Define the timestep (dt) and the total simulation time (t_max)
dt = 60  # 1 minute timestep
t_max = 3600 * 1 * 12   # 1 day of simulation

# Initialize the pygame library
pygame.init()

# Set the window size and title
width, height = 800, 600
pygame.display.set_mode((width, height))
pygame.display.set_caption("Orbit Simulation")

# Set the initial position and velocity
x = x0
y = y0
vx = vx0
vy = vy0

# Simulate the orbit of the spacecraft
for t in range(0, t_max, dt):
  # Calculate the distance between the spacecraft and the center of the Earth
  r = math.sqrt(x**2 + y**2)

  # Calculate the acceleration due to gravity
  ax = -G * M * x / r**3
  ay = -G * M * y / r**3

  # Update the velocity of the spacecraft
  vx += ax * dt
  vy += ay * dt

  # Update the position of the spacecraft
  x += vx * dt
  y += vy * dt

  # Draw the orbit on the screen
  pygame.draw.circle(
    pygame.display.get_surface(),  # surface
    (255, 255, 255),  # color
    (int(width/2 + x/R * 100), int(height/2 - y/R * 100)),  # position
    2,  # radius
    1,  # width (make the orbit path line thinner)
  )

  # Draw the Earth on the screen
  pygame.draw.circle(
    pygame.display.get_surface(),  # surface
    (0, 0, 255),  # color
    (int(width/2), int(height/2)),  # position
    5,  # radius
  )

  # Update the screen
  pygame.display.flip()

  # Slow down the simulation speed
  pygame.time.delay(100)
