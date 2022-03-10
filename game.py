#from colorama import init, Back
import random
from word_game.words import word_list

#init()

loop = True
while loop:
    print("Would you like to start a new game? Type 'yes' to start, type 'no' to exit.")
    start_input = input()
    if start_input == "no":
        loop = False
    elif start_input == 'yes':
        round_count = 0
        word_list_trial = ["cigar"]
        #to_guess = random.choice(word_list_trial)
        to_guess = "cigar"
        print("Enter a word of 5 letters")
        while round_count < 6:
            guessed = input()
            evaluated = ""
            for i in range(len(to_guess)):
                if guessed[i] == to_guess[i]:  # correct letter at correct position
                    evaluated = evaluated + guessed[i]
                else:  # wrong letter
                    evaluated = evaluated + '*'
            print(evaluated)
            if guessed == to_guess: #  if the guess is correct at the first try, we don't need the  for loop...? 
                print("You guessed correctly!")
                break
            round_count = round_count + 1
    else:
        print("You had a typo. Would you like to start a new game? Type 'yes' to start, type 'no' to exit.")    

