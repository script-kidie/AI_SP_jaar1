# klas v1b 
# student = Bram van leusden
# studentnummer = 1779320 

import random 

# color values chars are in dutch 
red = "R"
blue = "B"
green = "G"
white = "W"
orange = "O"
purple = "P"
black = "Z"
silver= "S"

color_lst = [red, blue, green, white, orange, purple, black, silver]

# asks player how many pins he/she wants in this round
correctlenght = False
while not correctlenght:
    length = input("hoeveel pinetjes lang wilt u de code hebben (max 5 minimaal 1):")
    try: length = int(length)

    except ValueError: 
        print(f"Geef een valide aantwoord")
        continue

    if 1 >= length or length < 6:
        correctlenght = True
        break
    else:
        print("incorrect aantal")
        continue

# asks player how many different colors he/she wants in this round
correctvariation = False   
while not correctvariation:
    variation = input("geef aan hoeveel vershillende kleuren pinnen u wilt(max 8 minimaal 1):")
    try: variation = int(variation)
    
    except ValueError:
        print("Geef een valide aantwoord")
        continue

    if 1 >= variation or variation < 9:
        print(variation)
        correctvariation = True
        break
    else:
        print("incorrect aantal")
        continue

print(f"Er zijn {variation} verschillende kleuren deze kleuren kunnen zijn rood, blauw, groen, wit, oranje, paars, zwart en silver" 
f"\n geef voor rood een R"
f"\n geef voor blauw een B"
f"\n geef voor groen een G"
f"\n geef voor wit een W"
f"\n geef voor oranje een O" 
f"\n geef voor paars een P"
f"\n geef voor zwart een Z"
f"\n geef voor silver een S")



def generate_code(length, variation, color_lst):
    """
      generates a list with color code where the length and color variation is specified by the player

      @returns lst  
    """
    code = []

    for i in range(length):
        x = random.randint(0, variation-1)
        code.append(color_lst[x])
    return code 


def guess_code(length, variation):
    """
    asks the player to give a color combinations and depending on the players answers gives feedback.

    @return True
    """
    answer = False
    code = generate_code(length,variation,color_lst)
    print(f"code={code}")
    while not answer:
        x = 0
        val1 = 0
        val2 = 0
        guess_lst = []
        guess = input(f"welke kleur combinatie denk je dat de geheime code is? (er zijn {length} pinnen en {variation} vershillende kleur(en)):")
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
                    val1 +=1
                    x += 1
                    continue 
                elif guess_lst[x] in code and guess_lst[x] != code[x]:
                    val2 +=1
                    x += 1 
                    continue

        print(f"Er zijn {val1} kleur(en) op de correcte plaats\n Er zijn {val2} kleur(en) juist maar op de verkeerde positie") 


    
guess_code(length, variation)
                 
