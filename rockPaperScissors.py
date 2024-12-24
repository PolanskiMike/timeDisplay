import random
choices = ['scissors','rock','paper']
choices.append('lizard')
choices.append('spok')

computerChoice = random.choice(choices)

userChoice = input("Do you want rock, paper, or scissors?\n")

if computerChoice == userChoice:
    print('TIE')
elif userChoice == 'rock' and computerChoice == 'scissors':
    print('WIN')
elif userChoice == 'paper' and computerChoice == 'rock':
    print('WIN')
elif userChoice == 'scissors' and computerChoice == 'paper':
    print('WIN')
elif userChoice == 'lizard' and computerChoice == 'spok':
    print('WIN')
elif userChoice == 'spok' and computerChoice == 'lizard':
    print('WIN')
else:
    print('LOSE')

print(computerChoice)