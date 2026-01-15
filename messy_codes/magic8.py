import random

Question= str(input("Question: "))
ans= ['Yes - definitely.',
'It is decidedly so.','Without a doubt.','Reply hazy, try again.','Ask again later.','Better not tell you now.','My sources say no.','Outlook not so good.','Very doubtful.']

print('Magic 8 Ball: '+ random.choice(ans))