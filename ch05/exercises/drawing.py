import turtle

def drawEqShape(myturtle, num_sides, side_length):
  myturtle = turtle.Turtle()
  myturtle.shape("turtle")
  myturtle.color("green")
  screen = turtle.Screen()
  screen.screensize(400,400)
  screen.bgcolor("white")
  for i in range(num_sides):
    myturtle.forward(side_length)
    myturtle.left(360 / num_sides)
  screen.exitonclick()


test = turtle.Turtle()
drawEqShape(test, 4, 50)

