import turtle #1. import modules
import random
# import pygame
# pygame.init()
# window = pygame.display.set_mode()
# import math


#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)


## 5. Your PART A code goes here
random = random.randrange(1,100)

michelangelo.forward(random)
leonardo.forward(random)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

for i in range(10):
  michelangelo.forward(random)
  leonardo.forward(random)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)


# PART B - complete part B here
# coords = []
# num_sides = input("Choose a number of sides. ")
# side_length = input("Choose the length of each side. ")


window.exitonclick()
