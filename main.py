from mastermind import *
import time

colors = ["Blauw", "Geel", "Groen", "Rood", "Wit", "Zwart"] 



while True: # Loop om te kiezen met hoeveel kleuren je het spel speelt.
    try:
        amount_of_colors = int(input("Met hoeveel kleuren ga je spelen?"))
        if 4 <= amount_of_colors <= 6:
            break
        print("waarde moet tussen 4 en 6")
    except:
        print("voer een getal in.")

possible_list = create_all_possible(colors[:amount_of_colors])

""" 
Opzet van de tests van de strategiën:

    - Spel wordt gespeeld voor ieder mogelijk antwoord van het spel.
    - Alle aantal pogingen worden onthouden in een dictionary.
    - Het gemiddelde wordt berekend over alle pogingen.
    - Tijd wordt gemeten om het aantal seconden te meten hoelang de strategiën duren.
"""
print("\nStarting random strategy\n")
start = time.time()
total_attempts = 0
attempt_table_random = dict()

for item in possible_list:
    outcome = make_guess(possible_list,item)
    total_attempts += outcome[1]
    if outcome[1] in list(attempt_table_random.keys()):
        attempt_table_random[outcome[1]] += 1
    else:
        attempt_table_random[outcome[1]] = 1

end = time.time()

print(f"finished random in {end - start} seconds.")
print(f"Average: {total_attempts/len(possible_list)}.")
print(f"Attempt count: {attempt_table_random}.")

print("\nStarting simple strategy\n")
start = time.time()
total_attempts = 0
attempt_table_simple = dict()

for item in possible_list:
    outcome = make_guess(possible_list,item, "simple")
    total_attempts += outcome[1]
    if outcome[1] in list(attempt_table_simple.keys()):
        attempt_table_simple[outcome[1]] += 1
    else:
        attempt_table_simple[outcome[1]] = 1

end = time.time()


print(f"finished Simple in {end - start} seconds.")
print(f"Average: {total_attempts/len(possible_list)}.")
print(f"Attempt count: {attempt_table_simple}.")
print("\n\nStarting most parts strategy\n")

start = time.time()
total_attempts = 0
attempt_table_most_parts = dict()

for item in possible_list:
    outcome = make_guess(possible_list,item,"most parts")
    total_attempts += outcome[1]
    if outcome[1] in list(attempt_table_most_parts.keys()):
        attempt_table_most_parts[outcome[1]] += 1
    else:
        attempt_table_most_parts[outcome[1]] = 1

end = time.time()

print(f"finished most parts in {end - start} seconds.")
print(f"Average: {total_attempts/len(possible_list)}.")
print(f"Attempt count: {attempt_table_most_parts}.")
print("\n\nStarting worst case strategy\n")

start = time.time()
total_attempts = 0
attempt_table_worst_case = dict()

for item in possible_list:
    outcome = make_guess(possible_list,item,"worst case")
    total_attempts += outcome[1]
    if outcome[1] in list(attempt_table_worst_case.keys()):
        attempt_table_worst_case[outcome[1]] += 1
    else:
        attempt_table_worst_case[outcome[1]] = 1

end = time.time()

print(f"finished worst case in {end - start} seconds.")
print(f"Average: {total_attempts/len(possible_list)}.")
print(f"Attempt count: {attempt_table_worst_case}.")
print("\nDone.")