def star_pyramid(): 
  stars = "*"
  numrows = int(input("Type a number of rows. "))
  for i in range(numrows):
    print(stars)
    print("\n")
    stars += "*"

def rstar_pyramid():
  rnumrows = int(input("Type a number of reverse rows. "))
  stars = "*" * rnumrows  
  for i in range(rnumrows):
    print(stars)
    print("\n")
    stars = stars[:-1]

star_pyramid()
rstar_pyramid()