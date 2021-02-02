import random


# opdracht 1 

def pyramide_for():
    hoogte = int(input("Hoeg moet de piramide worden"))
    ster = ""
    lst = []
    var = hoogte
    for i in range(hoogte):
        ster += "*"
        lst.append(ster)
        print(ster)
        if len(ster) == hoogte:
            for i in range(hoogte-1):
                var -= 1 
                lst.pop()[var]
                print(lst[len(lst)-1])


""" 
Ik heb hier uitgevonden dat je strings kunt vermenigvuldigen 
"""
        
def pyramide_while():
    hoogte = int(input("Hoeg moet de piramide worden"))
    x = 1
    y = hoogte 
    while x != hoogte+1: 
        print(x * "*")
        x += 1
        while x == hoogte+1:
            y -= 1
            print(y * "*")
            if y == 0: 
                break

#opdracht 2  

def difference_check():
    i = 0
    string1 = input("typ uw eerste string in:")
    string2 = input("typ uw tweede string in:")
    if string1 == string2:
        return "De strings zijn gelijk"
    else: 
        for s in string1:
            if i != len(string1)-1 and i != len(string2)-1:
                if s == string2[i]:
                    print(f"s={s}\n string2[i] = {string2[i]} i={i}")
                    i += 1
                else: 
                    return f"Bij index {i} is er een verschil1"
            else: 
                return f"Bij index {i+1} is er een verschil"


# opdracht 3  

lst = [1,2,3,4,5,6,7,7,8,9,0,0,0,0,7,6,6,66,66,444]
target = 66

def count(target, lst):
    x = 0 
    for i in lst:
        if target == i:
            x += 1
    return x

def highest_difference(lst):
    difference_lst = []

    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            difference_lst.append(lst[i+1] - lst[i])
        elif lst[i] > lst[i+1]:
             difference_lst.append(lst[i] - lst[i+1])
    return max(difference_lst)

def one_zero_check():
    zero_one_lst = [1,0,1]
    one_count = count(1, zero_one_lst)
    zero_count = count(0, zero_one_lst)

    if zero_count > one_count or zero_count > 12:
        return False
    else:
        return True


# opdracht 4  

def palindroom():
    woord = "radar"
    return woord == woord[::-1]

# opdracht 5

unsorted_lst = [12,345,546,546,122,343,777,888,454,333,212,444,666,878]

def simple_sort_lst(lst):

    return sorted(lst)

def my_sort_lst(lst):

    for i in range(len(lst)):
        x = i
        y = i + 1
        if y == len(lst):
            return lst
        elif lst[x] > lst[y]:
            swap = True
            lst[x], lst[y] = lst[y], lst[x]
            if swap:
                lst = sort_lst(lst)

# opdracht 6
 
average_lst = [1,2,3]

def average_list(lst):
   mean =  sum(lst) / len(lst)
   return f"het gemiddle van del lijst is {mean}"


more_average_lst = [[3,5,4,6,7],[3,4,5,6,2,4],[1,23,4,23,24,5]]

def many_average_list(lst):
    x = 0
    for i in lst:
        x += 1
        mean = sum(i) / len(i)
        print(f"het gemiddle van del lijst:{x} is {mean}")


# opdracht 7

def guesser():
    
    number = random.randint(1, 10)
    guess = int(input("Welk nummer denk u dat het getal is 1t/m10: "))

    while True:
        if guess == number:
            print("Succes u heeft het nummer geraden!")
            break
        else:
            guess = int(input("Helaas Fout geraden probeer het opnieuw! "))

# opdracht 8 

file = "data.txt"
"""
Ik krijg deze code niet werkend ook met code van anderen die wel werkt,
werkte hun codes niet op mijn computer 
"""
def compresinator(file):

    with open(file, "r") as file:
        file_text = file.read()
        
        print(file_text)
        replacement = file_text.replace(" ", "")
        replacement2 = replacement.replace("\n", "")


# opdracht 9

def cyclebits():

    ch = "b"
    val = random.randint(-4,4)
    print(f"val={val}")
    binary_lst = []

    binary = ' '.join(map(bin,bytearray(ch,encoding='utf-8')))
    binary2 = binary.replace("b", "")

    for i in binary2:
        binary_lst.append(i)
    if val > 0:
        for i in range(val):
            binary_lst.insert(8, binary_lst[0])
            binary_lst.pop(0)
    elif val < 0:
        val = val * -1
        for i in range(val):
            binary_lst.insert(0, binary_lst[7])
            binary_lst.pop(8)
    
    print(f"verschoven={binary_lst}")

# opdracht 10 

def fib(n):
    return fib(n-1) + fib(n-2) if n > 1 else (0, 1) [n]

# opdracht 11

def ceaser_cipher():

    shift = int(input("Geef een rotatie aan:"))
    txt = input("Voer uw tekst in:")
    txt2 = txt.lower()
    cipher_text = ""

    for c in txt2:
        if c.isalpha():
            ord_nummer = ord(c) + shift 
            if ord_nummer > ord("z"):
                ord_nummer -= 26
            cipher_letter = chr(ord_nummer)
            cipher_text += cipher_letter
            print(cipher_text)
    
    print(f"Orgineel:{txt}\nCeaser encryptie:{cipher_text}")

ceaser_cipher()


# opdracht 12 

def FizzBuzz():
    for i in range(1, 100):
        if i%3 == 0 and i%5 == 0:
            print("fizzbuzz")
        elif i%5 == 0:
            print("buzz")
        elif i%3 == 0: 
            print("fizz") 
        else:
            print(i)
