import pygame
import math
import random


## PART A - CREATING DARTBOARD ##
pygame.init()
window = pygame.display.set_mode((500, 400))
color = pygame.Color(255,150,150)
bg = pygame.Color(50,115,255)
pos = [200,200]
pygame.display.get_window_size()
window.fill(bg)
pygame.display.flip()
pygame.draw.circle(window,color, pos, 200, 0)
pygame.draw.line(window,'black', (200, 0), (200, 400))
pygame.draw.line(window,'black', (0, 200), (400, 200))
pygame.draw.line(window,'black', (400,0), (400,400))
pygame.display.update()


## PART B - DART GAME ##
d1color = 'red'
d2color = 'blue'
points1 = 0
points2 = 0
pchoice = 0 
redbox = pygame.Rect(420, 30, 60, 60)
bluebox = pygame.Rect(420, 300, 60, 60)
pygame.draw.rect(window, d1color, redbox)
pygame.draw.rect(window, d2color, bluebox)
pygame.display.update()
print("CHOOSE A COLOR")

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      x,y = pygame.mouse.get_pos()
      if pygame.Rect.collidepoint(redbox, (x,y)):
        print("Player 1 Selected")
        pchoice = pchoice + 1
        running = False
      if pygame.Rect.collidepoint(bluebox, (x,y)):
        print("Player 2 Selected")
        pchoice = pchoice + 2
        running = False
    if event.type == pygame.QUIT:
      running = False


for i in range(10):
  p1x = random.randrange(0,400)
  p1y = random.randrange(0,400)
  dart1 = [p1x, p1y]
  p2x = random.randrange(0,400)
  p2y = random.randrange(0,400)
  dart2 = [p2x, p2y]
  
  dcenter1 = math.hypot(200-p1x, 200-p1y)
  dcenter1 = round(dcenter1)
  incircle1 = dcenter1 <= 200
  if incircle1 == True:
    points1 = points1 + 1
  else:
    d1color = 'black'
  pygame.draw.circle(window, d1color, dart1, 5, 0)
  pygame.display.update()
  pygame.time.wait(500)

  dcenter2 = math.hypot(200-p2x, 200-p2y)
  dcenter2 = round(dcenter2)
  incircle2 = dcenter2 <= 200
  if incircle2 == True:
    points2 = points2 + 1
  else:
    d2color = 'black'
  pygame.draw.circle(window, d2color, dart2, 5, 0)
  pygame.display.update()
  pygame.time.wait(500)
  
  d1color = 'red'
  d2color = 'blue'

## PART C - SCORING ##
if pchoice == 1:
  if points1 > points2:
    print("Player 1 Wins!")
    print("Player 1 Score: " + str(points1))
    print("You Guessed Correctly!")
  elif points2 > points1:
    print("Player 2 Wins!")
    print("Player 2 Score: " + str(points2))
    print("You Guessed Incorrectly!")
  elif points1 == points2:
    print("Player 1 Score: " + str(points1))
    print("Player 2 Score: " + str(points2))
    print("It's a Tie!")
if pchoice == 2:
  if points1 > points2:
    print("Player 1 Wins!")
    print("Player 1 Score: " + str(points1))
    print("You Guessed Incorrectly!")
  elif points2 > points1:
    print("Player 2 Wins!")
    print("Player 2 Score: " + str(points2))
    print("You Guessed Correctly!")
  elif points1 == points2:
    print("Player 1 Score: " + str(points1))
    print("Player 2 Score: " + str(points2))
    print("It's a Tie!")
    

