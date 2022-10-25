class Goomba:
  def __init__(self,height,amount):
    self.goomba_quantity = amount
    self.goomba_height = (0,0.0)
    self.goomba_speed = 2

class Mario:
  def __init__(self, color, height):
    self.mario_color = color
    self.mario_height = height
    self.mario_speed = 5

class Laptop:
  def __init__(self,color):
    self.laptop_color = (0,0,0)
    self.is_laptop_on = False
    self.laptop_battery = 100