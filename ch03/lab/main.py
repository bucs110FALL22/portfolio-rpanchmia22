import turtle  #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')
michelangelo.speed(1)
leonardo.speed(1)

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

#5. Your PART A code goes here

michelangelo.forward(random.randrange(1,100))
leonardo.forward(random.randrange(1,100))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

for i in range(10):
  michelangelo.forward(random.randrange(1,100))
  leonardo.forward(random.randrange(1,100))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

window.exitonclick()

# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode()

color = pygame.Color(255, 255, 255)
coords = []
side_length = 50
offset = 200

sides = [3,4,6,9,360]

for s in sides:
  for i in range(s):
    theta = (2.0 * math.pi * i) / s
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    coords.append([x, y])
  window.fill("red")
  pygame.display.flip()
  pygame.draw.polygon(window,color,coords)
  pygame.display.flip()
  pygame.time.wait(1000)
  coords.clear()