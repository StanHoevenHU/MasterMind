import json
import random

def createAllPossible(colors):

    possibilities = list()

    for firstColor in range(len(colors)):
        for secondColor in range(len(colors)):
            for thirdColor in range(len(colors)):
                for forthColor in range(len(colors)):
                    possibilities.append([colors.copy()[firstColor],colors.copy()[secondColor],colors.copy()[thirdColor],colors.copy()[forthColor]])

    return possibilities

def giveAnswer(guess,answer):

    Black = 0
    White = 0
    answerCopy = answer.copy()
    guessCopy = guess.copy()

    for i in range(len(guessCopy)):
        if answerCopy[i] == guessCopy[i]:
            Black += 1
            answerCopy[i] = "Password Checked"
            guessCopy[i] = "Guess Checked"

    for i in range(len(guessCopy)):        
        if guessCopy[i] in answerCopy:
            White += 1
            answerCopy[answerCopy.index(guessCopy[i])] = "Password Checked"
            guessCopy[i] = "Guess Checked"
    
    return Black, White

def generateNextMoveMostParts(leftOverPossibilitiesMatrix):
    
    currentLongest = ""

    for item in leftOverPossibilitiesMatrix:
        if len(item[1]) > len(currentLongest):
            currentLongest = item[1]
            export = item[0]

    return export

def generateNextMoveWorstCase(leftOverPossibilitiesMatrix):

    worstCase = len(leftOverPossibilitiesMatrix)

    for item in leftOverPossibilitiesMatrix:
        highestValue = max(item[1].values())

        if highestValue < worstCase:
            worstCase = highestValue
    
    for item in leftOverPossibilitiesMatrix:
        if worstCase == max(item[1].values()):
            return item[0]

def generateMatrix(leftOverPossibilities,n):
    
    if n != 1:
        possibilityMatrix = list()
        
        for item in leftOverPossibilities:
            dictOfPossibilities = dict()

            for each in leftOverPossibilities:
                givenResponse = str(giveAnswer(item,each))

                if givenResponse in list(dictOfPossibilities.keys()):
                    dictOfPossibilities[givenResponse] += 1
            
                else:
                    dictOfPossibilities[givenResponse] = 1

            possibilityMatrix.append([item,dictOfPossibilities])

    else:

        with open("firstMatrix.json", "r") as JSONFile:
            possibleMatrixResponse = json.load(JSONFile)

        possibilityMatrix = possibleMatrixResponse
    
    return possibilityMatrix
    
def MakeGuess(leftOverPossibilities, password, gameMode = "", n = 1):
    
    listOfAnswers = list()

    if gameMode.lower() == "worst case":
        possibilityMatrix = generateMatrix(leftOverPossibilities,n)
        answerToGuess = generateNextMoveWorstCase(possibilityMatrix)

    elif gameMode.lower() == "most parts":
        possibilityMatrix = generateMatrix(leftOverPossibilities,n)
        answerToGuess = generateNextMoveMostParts(possibilityMatrix)
    
    elif gameMode.lower() == "simple":
        answerToGuess = leftOverPossibilities[0]
        
    else:
        answerToGuess = random.choice(leftOverPossibilities)

    Response = giveAnswer(answerToGuess,password)

    if Response == (4,0):
        return answerToGuess,n

    for item in leftOverPossibilities:
        checkResponse = giveAnswer(item,answerToGuess)
        if Response == checkResponse:
            listOfAnswers.append(item)

    return MakeGuess(listOfAnswers, password, gameMode, n+1)