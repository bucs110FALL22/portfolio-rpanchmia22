def main():
  score = int(input("Input a score: "))
  grade = percentage_to_letter(score)
  print(grade)
  passing = is_passing(grade)
  print(passing)
  if passing is True:
    print("You Passed!")
  else:
    print("You Failed!")

def percentage_to_letter(score=0):
  if score >= 90:
    return "A"
  elif 80 <= score < 90:
    return "B"  
  elif 70 <= score < 80:
    return "C"
  elif 60 <= score < 70:
    return "D"
  elif score < 60:
    return "F"

def is_passing(letter = None):
  if letter == "A":
    return(True)
  elif letter == "B":
    return(True)
  elif letter == "C":
    return(True)
  else:
    return(False)

main()