#Part 1
print("---------------------------------------------")
print(10 * 5)
print(10 ** 2)
print(15 / 10)
print(15 // 10)
print(-15 // 10)
print(15 % 10)
print(10 % 15)
print(10 % 10)
print(0 % 10)
print(10 / 15)
#The problem with this last answer is that after dividing, you get a infinitely repeating decimal. Yet when printed, the amount of sixes is only printed 16 times. This answer should be printed as an integer division function so that the answer is 0. 

#Part 2
print("---------------------------------------------")
rate = input("What is the current exchange rate for the Euro to Dollar? ")
amount = input("How much would you like to exchange? ")
total = (float(rate) * int(amount))
result = (float(total) - 3)
print("Your total is:",result)