import json
import random

def create_all_possible(colors):
    """
    Generen van alle mogelijken antwoorden.
    """

    possibilities = list()

    for first_color in range(len(colors)):
        for second_color in range(len(colors)):
            for third_color in range(len(colors)):
                for forth_color in range(len(colors)):
                    possibilities.append([colors.copy()[first_color],colors.copy()[second_color],colors.copy()[third_color],colors.copy()[forth_color]])

    return possibilities

def give_answer(guess,answer):
    """
    functie die 2 lijsten vergelijkt.
    Als de lijsten hetzelfde item op dezelfde locatie hebben, zwart optellen en de items uit lijst halen.
    Daarna checken of andere items nog in de lijsten overeen komen en aantal bijhouden in door wit op te tellen.
    Na hele lijst gechecked te hebben return de waarde van zwart en wit.
    """
    black = 0
    white = 0
    answer_copy = answer.copy()
    guess_copy = guess.copy()

    for i in range(len(guess_copy)):
        if answer_copy[i] == guess_copy[i]:
            black += 1
            answer_copy[i] = "Password Checked"
            guess_copy[i] = "Guess Checked"

    for i in range(len(guess_copy)):        
        if guess_copy[i] in answer_copy:
            white += 1
            answer_copy[answer_copy.index(guess_copy[i])] = "Password Checked"
            guess_copy[i] = "Guess Checked"
    
    return black, white

def generate_next_move_most_parts(left_over_possibilities_matrix):
    """
    Functie om grootste dictionary uit een lijst te halen.
    Return het corresponderende antwoord.
    """
    
    current_longest = ""

    for item in left_over_possibilities_matrix:
        if len(item[1]) > len(current_longest):
            current_longest = item[1]
            export = item[0]

    return export

def generate_next_move_worst_case(left_over_possibilities_matrix):
    """
    Functie om te bepalen welke lijst het kleinste getal bezit die in de lijst het grootst is.
    return het antwoord wat correspondeert met de bepaalde lijst.
    """

    worst_case = len(left_over_possibilities_matrix)

    for item in left_over_possibilities_matrix:
        highest_value = max(item[1].values())

        if highest_value < worst_case:
            worst_case = highest_value
    
    for item in left_over_possibilities_matrix:
        if worst_case == max(item[1].values()):
            return item[0]

def generate_matrix(left_over_possibilities,n):
    """
    Functie die een dictionary genereerd met alle mogelijke overgebleven responses van de giveAnswer functie van alle overgebleven antwoorden.
    Omdat bij de eerste poging alle antwoorden nog mogelijk zijn zal deze altijd hetzelfde zijn.
    Hierom is dit opgeslagen in een Json bestand en wordt dit ingelezen bij de eerste poging.
    """
    
    if n != 1:
        possibility_matrix = list()
        
        for item in left_over_possibilities:
            dict_of_possibilities = dict()

            for each in left_over_possibilities:
                given_response = str(give_answer(item,each))

                if given_response in list(dict_of_possibilities.keys()):
                    dict_of_possibilities[given_response] += 1
            
                else:
                    dict_of_possibilities[given_response] = 1

            possibility_matrix.append([item,dict_of_possibilities])

    else:

        with open("firstMatrix.json", "r") as JSONFile:
            possible_matrix_response = json.load(JSONFile)

        possibility_matrix = possible_matrix_response
    
    return possibility_matrix
    
def make_guess(left_over_possibilities, password, game_mode = "", n = 1):
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
    
    list_of_answers = list()

    if game_mode.lower() == "worst case":
        possibility_matrix = generate_matrix(left_over_possibilities,n)
        answer_to_guess = generate_next_move_worst_case(possibility_matrix)

    elif game_mode.lower() == "most parts":
        possibility_matrix = generate_matrix(left_over_possibilities,n)
        answer_to_guess = generate_next_move_most_parts(possibility_matrix)
    
    elif game_mode.lower() == "simple":
        answer_to_guess = left_over_possibilities[0]
        
    else:
        answer_to_guess = random.choice(left_over_possibilities)

    response = give_answer(answer_to_guess,password)

    if response == (4,0):
        return answer_to_guess,n

    for item in left_over_possibilities:
        check_response = give_answer(item,answer_to_guess)
        if response == check_response:
            list_of_answers.append(item)

    return make_guess(list_of_answers, password, game_mode, n+1)