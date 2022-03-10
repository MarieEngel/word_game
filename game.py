from colorama import Back
import random
from words import word_list


def create_game(word_list):
    return {"word": random.choice(word_list), "guesses": 6}


def evaluate_guess(to_guess, guessed):
    evaluated = ""
    for i in range(len(to_guess)):
        if guessed[i] == to_guess[i]:
            evaluated = evaluated + Back.GREEN + guessed[i] + Back.RESET
        elif guessed[i] in to_guess:
            evaluated = evaluated + Back.BLUE + guessed[i] + Back.RESET
        else:
            evaluated = evaluated + guessed[i]
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
            game = create_game(word_list)

            print("Enter a word of 5 letters")
            while game["guesses"] > 0:
                guessed = input()
                print(evaluate_guess(game["word"], guessed))
                if guessed == game["word"]:
                    print("You guessed correctly!")
                    break
                game["guesses"] -= 1
        else:
            print(
                "You had a typo. Would you like to start a new game? Type 'yes' to start, type 'no' to exit."
            )


if __name__ == "__main__":
    main()
