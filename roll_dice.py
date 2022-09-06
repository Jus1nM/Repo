import random
roll = random.randint(1,6)
guess = int(input('Guess the dice roll:\n'))
if guess != roll:
    print("Wrong! They roled a " + str(roll))
else:
    print("Right! They rolled a " + str(roll)) 
       