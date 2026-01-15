#https://www.codedex.io/python/16-sorting-hat

Gryffindor= 0
Ravenclaw= 0
Hufflepuff= 0
Slytherin= 0

print("Q1) Do you like Dawn or Dusk")
question1= int(input(" 1) Dawn\n 2) Dusk\n"))
if question1 == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif question1 ==2:
  Hufflepuff += 1
  Slytherin += 1
else :
  print("Wrong input\n")

print("Q2) When I'm dead, I want people to remember me as:\n 1) The Good\n 2) The Great\n 3) The Wise\n 4) The Bold\n")
question2= int(input())
if question2 ==1 :
  Hufflepuff += 2
elif question2 == 2 :
  Slytherin += 2
elif question2 ==3 :
  Ravenclaw +=2
elif question2 == 4:
  Gryffindor += 2
else :
  print("Wrong input \n")

print("Q3) Which kind of instrument most pleases your ear?\n 1) The violin\n 2) The trumpet\n 3) The piano\n 4) The drum\n")
question3= int(input())
if question3 == 1 :
  Slytherin += 4
elif question3 ==2 :
  Hufflepuff += 4
elif question3 ==3 :
  Ravenclaw += 4
elif question3 == 4 :
  Gryffindor += 4
else :
  print("Wrong input\n")

print("Gryffindor = "+ str(Gryffindor)+ "\n")
print("Ravenclaw = "+ str(Ravenclaw)+"\n")
print("Hufflepuff = "+ str(Hufflepuff)+ "\n")
print("Slytherin = "+ str(Slytherin)+ "\n")


