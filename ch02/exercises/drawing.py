import turtle

myturtle = turtle.Turtle()
screen = turtle.Screen()
screen.screensize(400,400)
screen.bgcolor("white")

sides = input("Input the number of sides for your shape. ")
sides = int(sides)
length = input("Input the length of each side. ")
length = int(length)

myturtle.shape("turtle")
myturtle.color("red")

for i in range(sides):
  myturtle.forward(length)
  myturtle.left(360 / sides)

screen.exitonclick()