# &= and
# |= or
# != not

height= int(input())
credits= int(input())

hc= height >= 137
cr= credits >= 10

if hc and cr :
  print('Enjoy the ride!')
elif not hc and cr :
  print('You are not tall enough to ride.')
elif hc and not cr :
  print("You don't have enough credits.")
else :
  print("You aren't met either requirement.")
