import Shelter

def main():
  buster = Shelter.Shelter("Buster", "Dog")
  q1 = str(input("Was this animal adopted today? Yes or No "))
  if q1 == "no":
    q2 = str(input("What day of the month was this animal adopted? "))
    q3 = str(input("What month was this animal adopted? "))
    q4 = str(input("What year was this animal adopted? "))
    buster.adopted(q2, q3, q4)
  print(buster.information())

main()