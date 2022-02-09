import random

colors = ["Green", "Yellow", "Red", "Blue", "black","Purple"]

possibilities = []
for i in range(6):
    for j in range(6):
        for k in range(6):
            for n in range(6):
                possibility = []
                possibility.append(colors[i])
                possibility.append(colors[j])
                possibility.append(colors[k])
                possibility.append(colors[n])
                possibilities.append(possibility)

password = random.choice(possibilities)

def giveAnswer(guess):
    Black = 0
    White = 0
    passwordCopy = password.copy()
    for i in range(len(guess)):
        if passwordCopy[i] == guess[i]:
            Black += 1
            passwordCopy[i] = "Password Checked"
            guess[i] = "Guess Checked"
    
    for i in range(len(guess)):        
        if guess[i] in passwordCopy:
            White += 1
            passwordCopy[password.index(guess[i])] = "Password Checked"
            guess[i] = "Guess Checked"
    return [Black, White]


def MakeGuess(leftOverPossibilities):
    listOfAnswers = []
    for each in leftOverPossibilities:
        listOfAnswers.append(giveAnswer(each))




print(password)
print()
guess1 = random.choice(possibilities)
guess2 = random.choice(possibilities)
guess3 = random.choice(possibilities)
guess4 = random.choice(possibilities)
guess5 = random.choice(possibilities)
guess6 = random.choice(possibilities)
print(guess1)
print(giveAnswer(guess1))
print(guess2)
print(giveAnswer(guess2))
print(guess3)
print(giveAnswer(guess3))
print(guess4)
print(giveAnswer(guess4))
print(guess5)
print(giveAnswer(guess5))
print(guess6)
print(giveAnswer(guess6))