import random

colors = ["Rood", "Blauw", "Groen", "Geel", "Zwart","Wit"] 
def createAllPossible():

   
    possibilities = []

    for firstColor in range(6):
        for secondColor in range(6):
            for thirdColor in range(6):
                for forthColor in range(6):
                    possibility = []
                    possibility.append(colors.copy()[firstColor])
                    possibility.append(colors.copy()[secondColor])
                    possibility.append(colors.copy()[thirdColor])
                    possibility.append(colors.copy()[forthColor])
                    possibilities.append(possibility)
    
    return possibilities

def giveAnswer(guess,answer):

    Black = 0
    White = 0
    passwordCopy = answer.copy()
    guessCopy = guess.copy()

    for i in range(len(guessCopy)):
        if passwordCopy[i] == guessCopy[i]:
            Black += 1
            passwordCopy[i] = "Password Checked"
            guessCopy[i] = "Guess Checked"

    for i in range(len(guessCopy)):        
        if guessCopy[i] in passwordCopy:
            White += 1
            passwordCopy[passwordCopy.index(guessCopy[i])] = "Password Checked"
            guessCopy[i] = "Guess Checked"
    return [Black, White]

def generatePossibleAnswers(guess,leftOvers):

    listOfPossibilities = dict()

    for each in leftOvers:
        givenResponse = str(giveAnswer(guess,each))

        if givenResponse in list(listOfPossibilities.keys()):
            listOfPossibilities[givenResponse] += 1
        else:
            listOfPossibilities[givenResponse] = 1

    return listOfPossibilities

def generateNextMoveMostParts(allPossibilities):
    export = ""
    currentLongest = ""

    for each in allPossibilities:
        if len(each[1]) > len(currentLongest):
            currentLongest = each[1]
            export = each
    return export


def generateNextMoveWorstCase(allPossibilities):

    worstCase = len(allPossibilities)

    for each in allPossibilities:
        highestValue = max(each[1].values())

        if highestValue < worstCase:
            worstCase = highestValue
    
    for each in allPossibilities:
        if worstCase in each[1].values():
            return each
    
def possibleMatrix(leftOverpossible):
    possibilityMatrix2 = []
    for each in leftOverpossible:
            possibilityMatrix2.append([each,generatePossibleAnswers(each,leftOverpossible)])
    return possibilityMatrix2

def MakeGuess(leftOverPossibilities, password, n):
    if len(leftOverPossibilities) <= 1:
        return leftOverPossibilities[0],n
    else:
        listOfAnswers = []
        if n != 1:
            possibilityMatrix = []
            for each in leftOverPossibilities:
                possibilityMatrix.append([each,generatePossibleAnswers(each,leftOverPossibilities)])
        else:
            possibilityMatrix = possibleMatrixResponse
        
        answerToGuess = generateNextMoveWorstCase(possibilityMatrix)[0]

        """
        answerToGuess = leftOverPossibilities[0]
        """
        theResponse = giveAnswer(answerToGuess,password)

        if theResponse == [4,0]:
            return answerToGuess,n

        for each in leftOverPossibilities:
            checkResponse = giveAnswer(each,answerToGuess)
            if theResponse == checkResponse:
                listOfAnswers.append(each)

        return MakeGuess(listOfAnswers, password, n+1)



possibleList = createAllPossible()
print("Kies de kleuren op basis van het indexgetal.\n1: Rood 2: Blauw 3: Groen 4: Geel 5: Zwart 6: Wit")
Color1 = int(input("Kleur 1\n-")) % 6 - 1
Color2 = int(input("Kleur 2\n-")) % 6 - 1
Color3 = int(input("Kleur 3\n-")) % 6 - 1
Color4 = int(input("Kleur 4\n-")) % 6 - 1

password = [colors.copy()[Color1],colors.copy()[Color2],colors.copy()[Color3],colors.copy()[Color4]]

possibleMatrixResponse = possibleMatrix(possibleList)

outcome = MakeGuess(possibleList,password,1)

print(f"Gevonden in {outcome[1]} pogingen. het antwoord is {outcome[0]}")
