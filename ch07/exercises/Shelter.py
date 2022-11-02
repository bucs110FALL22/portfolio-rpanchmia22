import time

class Shelter:
  def __init__(self, name, species):
    self.name = str(name)
    self.species = str(species)
    self.date_adopted = time.strftime("%d/%m/%y")
    self.id = id(self)
  
  def adopted(self, dd, mm, yy):
    self.date_adopted = str(dd) + "/" + str(mm) + "/" + str(yy)

  def information(self):
    return self.name, self.species, self.date_adopted, self.id