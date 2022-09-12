import turtle

myturtle = turtle.Turtle()
screen = turtle.Screen()
screen.screensize(400,400)
screen.bgcolor("white")


myturtle.shape("turtle")
myturtle.color("purple")
length = 50

for i in range(4):
  myturtle.forward(length)
  myturtle.left(90)

myturtle.color("red")
myturtle.penup()
myturtle.right(90)
myturtle.forward(length)
myturtle.pendown()
myturtle.left(90)

for i in range(4):
  myturtle.forward(length)
  myturtle.right(90)

screen.exitonclick()