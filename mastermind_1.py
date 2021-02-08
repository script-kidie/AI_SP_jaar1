# klas v1b 
# student = Bram van leusden
# studentnummer = 1779320 

# import library's 
import random 
import itertools

# ---- game functions and values ----- # 

# color values 
red = "R"
blue = "B"
green = "G"
white = "W"
purple = "P"
orange = "O"

color_lst = [red, blue, green, white, purple, orange]

# ask the player for the game type 
game_type = int(input("als u zelf wilt raden kies typ '1'\nals u de computer wil laten raden typ '2'\n"))


print(f"Er zijn 6 verschillende kleuren deze kleuren kunnen zijn rood, blauw, groen, wit, oranje en  paars" 
f"\n geef voor rood een R"
f"\n geef voor blauw een B"
f"\n geef voor groen een G"
f"\n geef voor wit een W"
f"\n geef voor oranje een O" 
f"\n geef voor paars een P")

length = 4
variation = 6


def generate_code(length, color_lst):
    """
      generates a list with a color code 

      @returns lst  
    """
    code = []

    for i in range(length):
        x = random.randint(0, 5)
        code.append(color_lst[x])
    return code 


def guess_code_player(length):
    """
    asks the player to give a color combinations and gives feedback depending on the players answer.

    @return no important returns 
    """
    answer = False
    code = generate_code(length,color_lst)
    black_lst = []
    black_lst2 = []

    while not answer:
        x = 0
        y = 0 
        val1 = 0
        val2 = 0
        guess_lst = []
        guess = input(f"welke kleur combinatie denk je dat de geheime code is?")
        guess = guess.upper()

        if len(guess) != length:
            print(f"uw antwoord moet {length} kleur(en) bevatten")
            continue
        else:    
            for c in guess:
                guess_lst.append(c)

            for i in range(length):
                if guess_lst == code:
                    print("Gefeliciteerd u heeft het antwoord correct geraden")
                    answer = True
                    return True
                elif guess_lst[x] == code[x]:
                    black_lst.append(code[x])
                    val1 +=1
                    x += 1
                    continue
                else: 
                    x += 1
                    continue
                for i in range(length): 
                    if (
                    guess_lst[y] in code 
                    and guess_lst[y] != code[y] 
                    and black_lst.count(guess_lst[y]) < black_lst2.count(guess_lst[y]) 
                    and black_lst2.count(guess_lst[y]) < code.count(guess_lst[y])
                    ):
                        black_lst2.append(guess_lst[y])
                        val2 +=1
                        y += 1 
                        continue
                    else: 
                        black_lst2.append(guess_lst[y])
                        y += 1 
                        continue

        print(f"Er zijn {val1} kleur(en) op de correcte plaats\nEr zijn {val2} kleur(en) juist maar op de verkeerde positie")

if game_type = 1: 
    guess_code_player(length)
                 
# ----- AI ----- #

def generate_posibilities():
    return(itertools.combinations(iterable, r))






