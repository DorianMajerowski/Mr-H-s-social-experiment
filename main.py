#FINISHED, turns out i just needed a short break from this project to almost instantly notice what i was doing wrong

#gets group name
groupName = input('What\'s the group name?: ')

#gets number of people in group
numOfPupils = int(input('How many people? (between 4 and 10): '))
#error checking for num of pupils
while numOfPupils < 4 or numOfPupils > 10:
  numOfPupils = int(input('i said between 4 and 10: '))

#get names for the number and do they want a photo?
names = []
ticketPrices = []
tempInput = ''
for x in range(numOfPupils):
  names.append(input('what\'s the name of pupil number ' + str(x + 1) + '?: '))
  tempInput = input('do they want a photo?(y/n): ')

  #error checking
  while tempInput.lower() != 'y' and tempInput.lower() != 'n':
    print('you dun goofed')
    tempInput = input('i said, do they want a photo?(y/n)!: ')

  #pretty self explanatory 
  if tempInput.lower() == 'y':
    ticketPrices.append('£4.99')
  else:
    ticketPrices.append('£3.00')

#prints all the necesarry info
print('your group is called ', groupName)
print('there are ', numOfPupils, ' people in your group')
print('and your ticket prices and names are: ')
for x in range(numOfPupils):
  print(names[x], '\t', ticketPrices[x])