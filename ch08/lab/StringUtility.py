class StringUtility():
  #INIT DEF#
  def __init__(self,string):
    self.str = string

  #STR DEF---------------------------#
  def __str__(self):
    return self.str

  #VOWELS DEF----------------------------------------#
  def vowels(self):
    vcount = 0
    for i in f"{self.str}":
      if i == "a":
        vcount += 1 
      elif i == "e" :
        vcount += 1 
      elif i == "i":
        vcount += 1 
      elif i == "o":
        vcount += 1 
      elif i == "u":
        vcount += 1  
      else:
        vcount += 0
    if vcount >= 5:
      vcount = "many"
    print(self.str,vcount)
    return str(vcount)

  #BOTH ENDS DEF-------------------------------------#  
  def bothEnds(self):
    return f"{self.str[:2]}" + f"{self.str[-2:]}"

  #FIX START DEF-------------------------------------#
  def fixStart(self):
    self.fix = list(self.str)
    vow = 1
    nul = ""
    for i in self.fix[1:]:
      if i is str(self.fix[0]):
        self.fix[vow]= "*"
        str(self.fix[vow])
      vow += 1
    return nul.join(self.fix)

  #ASCI SUM DEF-------------------------------------#
  def asciiSum(self):
    sum = 0
    for i in self.str:
      sum = sum + ord(i)
    return sum

  #CYPHER DEF---------------------------------------------------#
  def cipher(self): 
    num = len(self.str)
    newstr = ''
    for i in range(num):
      let = self.str[i]
      if let.isupper():
        newstr = newstr + chr((ord(let) + num - 65) % 26 + 65)
      elif let.islower():
        newstr = newstr +chr((ord(let)+ num - 97) % 26 + 97)
      else: 
        newstr = newstr + ' '
    return newstr