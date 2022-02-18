from MasterMind import *
import time

colors = ["Blauw", "Geel", "Groen", "Rood", "Wit", "Zwart"] 



while True: # Loop om te kiezen met hoeveel kleuren je het spel speelt.
    try:
        amountOfColors = int(input("Met hoeveel kleuren ga je spelen?"))
        if 4 <= amountOfColors <= 6:
            break
        print("waarde moet tussen 4 en 6")
    except:
        print("voer een getal in.")

possibleList = createAllPossible(colors[:amountOfColors])

""" 
Opzet van de tests van de strategiën:

    - Spel wordt gespeeld voor ieder mogelijk antwoord van het spel.
    - Alle aantal pogingen worden onthouden in een dictionary.
    - Het gemiddelde wordt berekend over alle pogingen.
    - Tijd wordt gemeten om het aantal seconden te meten hoelang de strategiën duren.
"""
print("\nStarting random strategy\n")
start = time.time()
totalAttempts = 0
attemptTableRandom = dict()

for item in possibleList:
    outcome = MakeGuess(possibleList,item)
    totalAttempts += outcome[1]
    if outcome[1] in list(attemptTableRandom.keys()):
        attemptTableRandom[outcome[1]] += 1
    else:
        attemptTableRandom[outcome[1]] = 1

end = time.time()

print(f"finished random in {end - start} seconds.")
print(f"Average: {totalAttempts/len(possibleList)}.")
print(f"Attempt count: {attemptTableRandom}.")

print("\nStarting simple strategy\n")
start = time.time()
totalAttempts = 0
attemptTableSimple = dict()

for item in possibleList:
    outcome = MakeGuess(possibleList,item, "simple")
    totalAttempts += outcome[1]
    if outcome[1] in list(attemptTableSimple.keys()):
        attemptTableSimple[outcome[1]] += 1
    else:
        attemptTableSimple[outcome[1]] = 1

end = time.time()


print(f"finished Simple in {end - start} seconds.")
print(f"Average: {totalAttempts/len(possibleList)}.")
print(f"Attempt count: {attemptTableSimple}.")
print("\n\nStarting most parts strategy\n")

start = time.time()
totalAttempts = 0
attemptTableMostParts = dict()

for item in possibleList:
    outcome = MakeGuess(possibleList,item,"most parts")
    totalAttempts += outcome[1]
    if outcome[1] in list(attemptTableMostParts.keys()):
        attemptTableMostParts[outcome[1]] += 1
    else:
        attemptTableMostParts[outcome[1]] = 1

end = time.time()

print(f"finished most parts in {end - start} seconds.")
print(f"Average: {totalAttempts/len(possibleList)}.")
print(f"Attempt count: {attemptTableMostParts}.")
print("\n\nStarting worst case strategy\n")

start = time.time()
totalAttempts = 0
attemptTableWorstCase = dict()

for item in possibleList:
    outcome = MakeGuess(possibleList,item,"worst case")
    totalAttempts += outcome[1]
    if outcome[1] in list(attemptTableWorstCase.keys()):
        attemptTableWorstCase[outcome[1]] += 1
    else:
        attemptTableWorstCase[outcome[1]] = 1

end = time.time()

print(f"finished worst case in {end - start} seconds.")
print(f"Average: {totalAttempts/len(possibleList)}.")
print(f"Attempt count: {attemptTableWorstCase}.")
print("\nDone.")