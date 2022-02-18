from MasterMind import *
import time

colors = ["Blauw", "Geel", "Groen", "Rood", "Wit", "Zwart"] 

while True:
    try:
        amountOfColors = int(input("Met hoeveel kleuren ga je spelen?"))
        if 4 <= amountOfColors <= 6:
            break
        print("waarde moet tussen 4 en 6")
    except:
        print("voer een getal in.")

possibleList = createAllPossible(colors[:amountOfColors])


print("\nStarting random strategy\n")
start = time.time()
totalAttempts = 0
attemptTableRandom = dict()

for item in possibleList:
    outcome = MakeGuess(possibleList,item)
    #print(f"Het antwoord is {item}. De bot vond in {outcome[1]} pogingen het volgende antwoord: {outcome[0]}")
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
    #print(f"Het antwoord is {item}. De bot vond in {outcome[1]} pogingen het volgende antwoord: {outcome[0]}")
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
    #print(f"Het antwoord is {item}. De bot vond in {outcome[1]} pogingen het volgende antwoord: {outcome[0]}")
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
    #print(f"Het antwoord is {item}. De bot vond in {outcome[1]} pogingen het volgende antwoord: {outcome[0]}")
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