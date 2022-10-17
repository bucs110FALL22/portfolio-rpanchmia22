def multiplication(num1, num2):
  mul = 0
  for i in range(1,num2+1):
    mul = mul + num1
  print(mul)

def exponent(num3, num4):
  mul = 1
  for i in range(1,num4+1):
    mul = mul * num3
  print(mul)

def square(sq): 
  multiplication(sq, sq)


print("Multiplication: ")
multiplication(3,6)
print("Exponent: ")
exponent(3,3)
print("Square: ")
square(8)
