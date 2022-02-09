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

#password = random.choice(possibilities)
password = [colors[4],colors[2],colors[2],colors[3]]
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
guess1 = [colors[1],colors[2],colors[3],colors[4]]
guess2 = [colors[5],colors[5],colors[1],colors[2]]
guess3 = [colors[2],colors[3],colors[4],colors[5]]
guess4 = [colors[1],colors[3],colors[1],colors[1]]
guess5 = [colors[5],colors[5],colors[5],colors[5]]
guess6 = [colors[4],colors[2],colors[2],colors[3]]
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
