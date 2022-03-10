# from colorama import init, Back
import random
from words import word_list

# init()
def get_word(word_list):
    to_guess = random.choice(word_list)
    return to_guess


def evaluate_guess(to_guess, guessed):
    evaluated = ""
    for i in range(len(to_guess)):
        if guessed[i] == to_guess[i]:
            evaluated = evaluated + guessed[i]
        else:
            evaluated = evaluated + "*"

    return evaluated


def main():
    while True:
        print(
            "Would you like to start a new game? Type 'yes' to start, type 'no' to exit."
        )
        start_input = input()
        if start_input == "no":
            break
        elif start_input == "yes":
            round_count = 0
            to_guess = get_word(word_list)
            print("Enter a word of 5 letters")
            while round_count < 6:
                guessed = input()
                print(evaluate_guess(to_guess, guessed))
                if guessed == to_guess:
                    print("You guessed correctly!")
                    break
                round_count = round_count + 1
        else:
            print(
                "You had a typo. Would you like to start a new game? Type 'yes' to start, type 'no' to exit."
            )


if __name__ == "__main__":
    main()
