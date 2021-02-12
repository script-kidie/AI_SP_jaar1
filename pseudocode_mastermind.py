"""
pseudocode simple strategy:


1. generate all possible mastermind codes 
2. put all possible codes in a list that can be editet 
3. make a list that is empty 
4. pick a random code from all the possible codes 
5. compare the guess with the player given code 
    5.1 if the amount of black pins is 4 
        5.1.1 say to the player that the ai guessed the code and 
        5.1.2 stop the application/procces  
    5.2 if the amount black pins in step 5.1 is not four compare all possible answers (i) with the guess
        5.2.1 if all items have been compared go to step 6  
        5.2.2 if in the comparison in step 7 the amount of blackpins + whitepins is the same as the comparison in step 5
            5.2.2.1 add i to the empty list 
            5.2.2.2 after putting i in the list of possible awnsers go to back to step 5.2 
        5.2.3 if the amount of blackpins + whitepins is not the same as in the comparison in step 5
            5.2.3.1 go to step 5.2  
6. pick a random code from all the added items to the list from step 3 and make this code the next guess
7. make the list from step 2 the same as the list used in step 6 
8. make the list from step 6 empty again 
9. go to step 5 and use the guess from step 6 
"""




"""
pseudocode worstcase: 


1. generate all possible mastermind codes 
2. put all possible codes in a list that can be editet 
3. make a list that is empty 
4. make a predetermind first guess 
5. compare the guess with the player given code 
    5.1 if the amount of black pins is 4 
        5.1.1 say to the player that the ai guessed the code and 
        5.1.2 stop the application/procces  
    5.2 if the amount black pins in step 5.1 is not four compare all possible answers (i) with the guess
        5.2.1 if all items have been compared go to step 6  
        5.2.2 if in the comparison in step 7 the amount of blackpins and whitepins is the same as the comparison in step 5
            5.2.2.1 add i to the empty list 
            5.2.2.2 after putting i in the list of possible awnsers go to back to step 5.2 
        5.2.3 if the amount of blackpins and whitepins is not the same as in the comparison in step 5
            5.2.3.1 go to step 5.2  
6. pick a random code from all the added items to the list from step 3 and make this code the next guess
7. make the list from step 2 the same as the list used in step 6
8. make the list from step 6 empty again 
9. go to step 5 and use the guess from step 6 
"""




"""
pseudocode van mijn eigen heuristiek:


1. generate all possible mastermind codes 
2. put all possible codes in a list that can be editet 
3. make a list that is empty 
4. make a list with 2 predetermind first guesses 
5. compare the guesses from step 4 for the first 2 iterations of this code after that use the guesses from step 6 with the player given code 
    5.1 if the amount of black pins is 4 
        5.1.1 say to the player that the ai guessed the code and 
        5.1.2 stop the application/procces  
    5.2 if the amount black pins in step 5.1 is not four compare all possible answers (i) with the guess
        5.2.1 if all items have been compared go to step 6  
        5.2.2 if in the comparison in step 7 the amount of blackpins and whitepins is the same as the comparison in step 5
            5.2.2.1 add i to the empty list 
            5.2.2.2 after putting i in the list of possible awnsers go to back to step 5.2 
        5.2.3 if the amount of blackpins and whitepins is not the same as in the comparison in step 5
            5.2.3.1 go to step 5.2  
6. pick a random code from all the added items to the list from step 3 and make this code the next guess
7. make the list from step 2 the same as the list used in step 8 
8. make the list from step 8 empty again 
9. go to step 5 and use the guess from step 6 
"""


