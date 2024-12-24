import random
choices = ['scissors','rock','paper']
choices.append('lizard')
choices.append('spok')

computerChoice = random.choice(choices)

numRounds = input("How many rounds do you want to play?\n")

userChoice = input("Do you want rock, paper, scissors, lizard, spok?\n")


for rounds in range(numRounds):
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
