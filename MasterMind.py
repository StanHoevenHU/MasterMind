import json
import random

def createAllPossible(colors):
    """
    Generen van alle mogelijken antwoorden.
    """

    possibilities = list()

    for firstColor in range(len(colors)):
        for secondColor in range(len(colors)):
            for thirdColor in range(len(colors)):
                for forthColor in range(len(colors)):
                    possibilities.append([colors.copy()[firstColor],colors.copy()[secondColor],colors.copy()[thirdColor],colors.copy()[forthColor]])

    return possibilities

def giveAnswer(guess,answer):
    """
    functie die 2 lijsten vergelijkt.
    Als de lijsten hetzelfde item op dezelfde locatie hebben, zwart optellen en de items uit lijst halen.
    Daarna checken of andere items nog in de lijsten overeen komen en aantal bijhouden in door wit op te tellen.
    Na hele lijst gechecked te hebben return de waarde van zwart en wit.
    """
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
    """
    Functie om grootste dictionary uit een lijst te halen.
    Return het corresponderende antwoord.
    """
    
    currentLongest = ""

    for item in leftOverPossibilitiesMatrix:
        if len(item[1]) > len(currentLongest):
            currentLongest = item[1]
            export = item[0]

    return export

def generateNextMoveWorstCase(leftOverPossibilitiesMatrix):
    """
    Functie om te bepalen welke lijst het kleinste getal bezit die in de lijst het grootst is.
    return het antwoord wat correspondeert met de bepaalde lijst.
    """

    worstCase = len(leftOverPossibilitiesMatrix)

    for item in leftOverPossibilitiesMatrix:
        highestValue = max(item[1].values())

        if highestValue < worstCase:
            worstCase = highestValue
    
    for item in leftOverPossibilitiesMatrix:
        if worstCase == max(item[1].values()):
            return item[0]

def generateMatrix(leftOverPossibilities,n):
    """
    Functie die een dictionary genereerd met alle mogelijke overgebleven responses van de giveAnswer functie van alle overgebleven antwoorden.
    Omdat bij de eerste poging alle antwoorden nog mogelijk zijn zal deze altijd hetzelfde zijn.
    Hierom is dit opgeslagen in een Json bestand en wordt dit ingelezen bij de eerste poging.
    """
    
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
    """
    Functie met meerdere delen.
    
    deel 1:
    Zorgt voor een antwoord op basis van de gekozen strategie.
    Bij de keuzes worst case en most parts, 
    wordt de keuze gemaakt op basis van de eerder bescheven functies waarbij eerst de lijsten met overgebleven mogelijkheden eerst worden gegenereerd.
    
    Deel 2:
    De gok wordt gedaan.
    Als de gok goed is, returnt de functie het juiste antwoord en het aantal pogingen.
    Als de gok niet goed is wordt de lijst gefiltert met alle mogelijkheden.
    
    Deel 3:
    De functie wordt recursief aangeroepen om de volgende gok te doen.
    Aan de functie worden de overgebleven antwoorden in een lijst meegegeven,
    Het juiste antwoord wordt opnieuw meegegeven,
    de huidige gamemode en het aantal beurten.
    """
    
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