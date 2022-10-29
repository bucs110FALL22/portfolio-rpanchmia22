import turtle

bob = turtle.Turtle()
bob.color('black')
screen = turtle.Screen()
screen.screensize(200,200)
screen.bgcolor("lightblue")

def main():
  base()
  roof()
  door()
  window()
  sun()
  grass()
  flowers()
  tohome()

def tohome():
  bob.penup()
  bob.goto(-150,-100)  
def drawbase(length,height):
  #This function draws the base of the house.
  for i in range(2):
    bob.forward(length)
    bob.left(90)
    bob.forward(height)
    bob.left(90)
  print("The length of the house is " + str(length))
  print("The height of the house is " + str(height))

def base():
  #This function tells the user to input a color for the base then uses the function drawbase() to draw the base of the house. 
  bcol = input("Pick a color for the base: ")
  tohome()
  bob.pendown()
  bob.fillcolor(bcol)
  bob.begin_fill()
  drawbase(200,150)
  bob.end_fill()




def roof():
  #This function tells the user to input a color for the roof, and then draws the roof. 
  rcol = input("Pick a color for the roof: ")
  tohome()
  bob.goto(-150,50)
  bob.pendown()
  bob.fillcolor(rcol)
  bob.begin_fill()
  bob.left(45)
  bob.forward(142)
  bob.right(90)
  bob.forward(142)
  bob.end_fill()
  bob.left(45)

def door():
  #This function tells the user to input a color for the door and then draws the door. 
  dcol = input("Pick a color for the door: ")
  tohome()
  bob.goto(15,-100)
  bob.left(90)
  bob.pendown()
  bob.fillcolor(dcol)
  bob.begin_fill()
  for i in range(2):
    bob.forward(35)
    bob.right(90)
    bob.forward(25)
    bob.right(90)
  bob.end_fill()
  bob.penup()
  bob.goto(35,-80)
  bob.pendown()
  bob.circle(2)


def window():
  #This function draws the window.
  tohome()
  bob.goto(-125,0)
  bob.pendown()
  bob.fillcolor('white')
  bob.begin_fill()
  for i in range(2):
    bob.right(90)
    bob.forward(100)
    bob.right(90)
    bob.forward(30)
  bob.end_fill()


def sun():
  #This function draws the sun.
  tohome()
  bob.goto(190,130)
  bob.pendown()
  bob.fillcolor('yellow')
  bob.begin_fill()
  bob.circle(50)
  bob.end_fill()


def grass():
  #This function draws the grass.
  tohome()
  bob.goto(-200,-100)
  bob.right(90)
  bob.pendown()
  bob.fillcolor('lightgreen')
  bob.begin_fill()
  for i in range(2):
    bob.forward(400)
    bob.right(90)
    bob.forward(100)
    bob.right(90)
  bob.end_fill()


def flowers():
  #This function tells the user to input a color for the flowers and then draws the flowers. 
  fcol = input("Pick a color for the flowers: ")
  flowcoord = [80,100,120,140,160]
  tohome()
  bob.fillcolor(fcol)
  bob.left(90)
  for f in flowcoord:
    bob.penup()
    bob.goto(f,-100)
    bob.pendown()
    bob.forward(15)
    bob.begin_fill()
    for i in range(4):
      bob.right(90)
      bob.circle(4,180)
    bob.end_fill()



main()
screen.exitonclick()

