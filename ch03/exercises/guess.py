import random

randnum = random.randint(1,10)

for i in range(3):
  guess = int(input("Pick a number from 1-10. "))
  if(guess == randnum):
    print("Correct!")
    break
    
  elif(guess > randnum):
    print("Incorrect! Too High.")

  elif(guess < randnum):
    print("Incorrect! Too Low.")

print("You lose!")