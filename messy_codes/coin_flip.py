import random

num= random.randint(0, 1)   # Generate a random number that is either 0 or 1
if num > 0.5:
  print("Heads")
else:
  print("Tails")