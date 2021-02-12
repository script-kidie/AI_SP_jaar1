# klas v1b 
# student = Bram van leusden
# studentnummer = 1779320 

# import library's 
import random 
import itertools
import time

# ---- values and functions that are used globaly in the code ---- #

# ask the player for the game type
while True: 
    game_type = input("als u zelf wilt raden kies typ '1'\nals u de computer wil laten raden typ '2'\n")
    try:
        game_type = int(game_type)
    except ValueError:
        print(f"geef een valide antwoord")
        continue
    if game_type > 3:
        print("geef een valide antwoord")
    else:
        break


# color values 
red = "R"
blue = "B"
green = "G"
white = "W"
purple = "P"
orange = "O"

color_lst = [red, blue, green, white, purple, orange]

print(f"Er zijn 6 verschillende kleuren deze kleuren kunnen zijn rood, blauw, groen, wit, oranje en paars" 
f"\n geef voor rood een R"
f"\n geef voor blauw een B"
f"\n geef voor groen een G"
f"\n geef voor wit een W"
f"\n geef voor oranje een O" 
f"\n geef voor paars een P")


def check_answer(code, guess):
    """
    compares the code and the guess and gives feedback on what was placed right or wrong. 

    @return int 
    """

    blackpin = 0
    whitepin = 0

    edit_code_lst = code.copy()
    edit_guess_lst = list(guess).copy()

    x = 0
    y = 0

    for i in guess:
        if i == code[x]:
            edit_code_lst[x] = 1
            edit_guess_lst[x] = 0
            blackpin +=1
        x +=1
    
    for i in edit_guess_lst:
        if i in edit_code_lst:
            edit_code_lst[edit_code_lst.index(i)] = 1
            edit_guess_lst[y] = 0
            whitepin += 1
        y += 1 

    return [blackpin, whitepin]

# ---- game functions where the player guesses (game type 1) ----- # 


def generate_code(color_lst):
    """
      generates a list with a color code 

      @returns lst  
    """
    code = []

    for i in range(4):
        x = random.randint(0, 5)
        code.append(color_lst[x])
    return code 


def guess_code_player():
    """
    asks the player to give a color combinations and gives feedback depending on the players answer.
    """
    code_ai = generate_code(color_lst)
    print(code_ai)

    while True:
        guess_lst = []
        guess = input("Hoe denk u dat de code er uit ziet:")
        guess = guess.upper()

        for c in guess:
            guess_lst.append(c)
        if guess_lst == code_ai:
            print("hoera u heeft het geraden")
            return True
        else:
            check_answer(code_ai, guess_lst)
            print(check_answer(code_ai, guess_lst))
            blackpins = check_answer(code_ai, guess_lst)[0]
            whitepins = check_answer(code_ai, guess_lst)[1] 
        print(f"er zijn {blackpins} correct en er zijn {whitepins} op de verkeerde plek")


        
# initates game mode one
if game_type == 1: 
    guess_code_player()

# ---- functions where the ai guesses game type 2 ---- # 


# asks the player for a code so the ai can crack it
if game_type == 2:
    master_code = []
    master_code_str = input("voer uw geheime code in:")
    master_code_str = master_code_str.upper()

    for c in master_code_str:
        master_code.append(c)
            
# ----- AI ----- #

def generate_possibilities():
    """
    generates all possible awnsers in a mastermind game

    @return lst
    """
    return list(itertools.product(color_lst, repeat=4))


def simple_strategy():
    """
    this is code for an ai that tries to guess the players code with the simple strategy
    """
    turn = 1

    possibilities = generate_possibilities()
    possible = []

    for i in possibilities:
        possible.append(list(i))

    possible_answers = possible.copy()
    possible_answers2 = []

    guess = random.choice(possible_answers)

    while True:    
        feedback_game = check_answer(master_code, guess)
        if feedback_game[0] == 4:
            print(f"De simple strategy heeft de code geraden op ronde {turn}") 
            return True
        for i in possible_answers:
            feedback_in_function = check_answer(guess, i)
            if feedback_in_function[0] + feedback_in_function[1] == feedback_game[0] + feedback_game[1]:
                possible_answers2.append(i)


        guess = random.choice(possible_answers2)
        possible_answers = possible_answers2.copy()
        possible_answers2 = []

        turn += 1


def worstcase():
    """
    an ai that uses the worstcase algorithm and guesses the player given code
    """
    turn = 1

    possibilities = generate_possibilities()
    possible = []

    for i in possibilities:
        possible.append(list(i))

    possible_answers = possible.copy()
    possible_answers2 = []

    guess = [red, red, blue, blue]

    while True:    
        feedback_game = check_answer(master_code, guess)

        if feedback_game[0] == 4:
            print(f"De worst case ai heeft de code geraden op ronde {turn}") 
            return True
        for i in possible_answers:
            feedback_in_function = check_answer(guess, i)
            if feedback_in_function[0] == feedback_game[0] and feedback_in_function[1] == feedback_game[1]:
                possible_answers2.append(i)


        guess = random.choice(possible_answers2)
        possible_answers = possible_answers2.copy()
        possible_answers2 = []

        turn += 1
    


def my_own_heuristic():
    """
    guesses the players code with a tactic i came up with  
    """
    turn = 1

    possibilities = generate_possibilities()
    possible = []

    for i in possibilities:
        possible.append(list(i))

    possible_answers = possible.copy()
    possible_answers2 = []

    intial_guesses = [[red,red,blue,blue],[green, green, white, white]]

    while True:
        if turn < 2:
            for i in intial_guesses:
                guess = i 
                feedback_game = check_answer(master_code, guess)
                if feedback_game[0] == 4:
                    print(f"De ai met mijn eigen heuristiek heeft het geraden op ronde {turn}")
                    return True     
                for i in possible_answers:
                    feedback_in_function = check_answer(guess, i)
                    if feedback_in_function[0] == feedback_game[0] and feedback_in_function[1] == feedback_game[1]:
                        possible_answers2.append(i)
                    else: 
                        continue
                possible_answers = possible_answers2
                possible_answers2 = []
                turn += 1
        if turn >= 3:
            guess = random.choice(possible_answers)
            feedback_game = check_answer(master_code, guess)
            if feedback_game[0] == 4:
                print(f"De ai heeft het geraden op ronde {turn}")
                return True
            for i in possible_answers:
                feedback_in_function = check_answer(guess, i)
                if feedback_in_function[0] == feedback_game[0] and feedback_in_function[1] == feedback_game[1]:
                    possible_answers2.append(i)
                else: 
                    continue
            possible_answers = possible_answers2
            possible_answers2 = []
            turn += 1

  
           

  

# ask the player witch ai he wants to play agianst
while game_type == 2:
    ai_choice = (input("voer het cijfer in voor de ai die u wilt uitproberen\n1: simple strategy\n2: worst case\n3: mijn eigen heuristiek\n"))
    try:
        ai_choice = int(ai_choice)
    except ValueError:
        print(f"geef een valide antwoord")
        continue
    if ai_choice == 1:
        simple_strategy()
        break
    elif ai_choice == 2:
        worstcase()
        break
    elif ai_choice == 3:
        my_own_heuristic()
        break
    else:
        print("geef een valide antwoord")

