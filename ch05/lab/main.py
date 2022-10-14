import pygame


pygame.init()
display = pygame.display.set_mode((400,400))
color = pygame.Color('black')
bg = pygame.Color("white")
display.fill(bg)
pygame.display.flip()
font = pygame.font.Font(None, 50)
start = 2
upper_limit = 100
iters = {}
max_so_far = 0
max_val = 0
SCALE = 5


for i in range(start, upper_limit+1):
  count = 0
  num = i
  while(i > 1):
    if(i % 2 == 0):
      i = i / 2
    elif(i % 2 == 1):
      i = (i * 3 + 1)
    count = count + 1
  iters[num * SCALE] = count * SCALE
  if count > max_so_far:
    max_so_far = count
    max_val = num
coordinates = list(iters.items())
print(iters)
print("Max value: " + str(max_val))
print("Max iteration: " + str(max_so_far))


pygame.draw.lines(display, color, False, coordinates)
new_display = pygame.transform.flip(display, False, True)
display.blit(new_display, (0,0))
msg = font.render(str(max_so_far), True, color)
display.blit(msg, (10,10))
pygame.display.update()
pygame.time.wait(5000)