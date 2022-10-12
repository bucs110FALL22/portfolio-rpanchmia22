start = int(input("Pick a start number. "))
upper_limit = int(input("Pick an end number. "))
iters = {}

for i in range(start, upper_limit+1):
  count = 0
  num = i
  while(i > 1):
    if(i % 2 == 0):
      i = i / 2
    elif(i % 2 == 1):
      i = (i * 3 + 1)
    count = count + 1
  iters[num] = count

print(iters)