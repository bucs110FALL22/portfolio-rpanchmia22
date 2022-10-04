import turtle
import random


animal = turtle.Turtle()
animal.color('green')
animal.shape('turtle')
animal.speed(1)


width = 200
height = 200
window = turtle.Screen()
window.screensize(width,height)
xx = animal.xcor()
yy = animal.ycor()


def cointoss():
    return random.choice(["Heads", "Tails"])


while xx > -100 and xx < 100 and yy > -100 and yy < 100:
  xx = animal.xcor()
  yy = animal.ycor()
  if(cointoss() == "Heads"):
    animal.left(90)
    animal.forward(50)
  if(cointoss() == "Tails"):
    animal.right(90)
    animal.forward(50)


window.exitonclick()