import random

game_choice = input("Would you like to play 'coin toss' or 'dice roll'?: ")
input_validation_game_choice = False

while(input_validation_game_choice == False):
    if(game_choice == "coin toss"):
        print("Okay, let's get started with the coin toss!")
        input_validation_game_choice = True
    elif(game_choice == "dice roll"):
        print("Okay, let's get started with the dice roll!")
        input_validation_game_choice = True
    else:
        game_choice = input(
            "Sorry, I didn't understand that. Do you want to play 'coin toss', or, 'dice roll'?: ")

if(game_choice == "coin toss"):
    play_again = True
    user_score = 0
    total_flips = 0
    options = ["Heads", "Tails"]

    while(play_again == True):
        heads_tails = random.randint(0, 1)
        if(total_flips == 0):
            print("Welcome to the coin toss game!")

        user_input = input(
            "Please enter 'Heads' or 'Tails' (case sensitive!): ")
        if(user_input == options[heads_tails]):
            print("You guessed correctly!")
            user_score += 1
            total_flips += 1
            print("Total guesses: " + str(total_flips) +
                  " Correct guesses: " + str(user_score))
        else:
            print("You did not guess correctly. Try again.")
            total_flips += 1
            print("Total guesses: " + str(total_flips) +
                  " Correct guesses: " + str(user_score))
        again = input("Would you like to play again? (Yes/No): ")

        input_validation_yes_no = False

        while(input_validation_yes_no == False):
            if(again == "No" or again == "no"):
                play_again = False
                input_validation_yes_no = True
                print("Thanks for playing! You got " + str(user_score) +
                      " correct out of " + str(total_flips) + " total coin tosses.")
            elif(again == "Yes" or again == "yes"):
                input_validation_yes_no = True
                continue
            else:
                print("Invalid input! Please enter yes or no.")
                again = input("Would you like to play again? (Yes/No): ")

if(game_choice == "dice roll"):
    play_again = True
    user_score = 0
    total_rolls = 0
    while(play_again == True):
        dice_result = random.randint(1, 6)
        if(total_rolls == 0):
            print("Welcome to the dice roll game!")

        user_input = int(input(
            "Please enter your guess from 1 - 6: "))
        if(user_input == dice_result):
            print("You guessed correctly!")
            user_score += 1
            total_rolls += 1
            print("Total guesses: " + str(total_rolls) +
                  " Correct guesses: " + str(user_score))
        else:
            print("You did not guess correctly. Try again.")
            total_rolls += 1
            print("Total guesses: " + str(total_rolls) +
                  " Correct guesses: " + str(user_score))
        again = input("Would you like to play again? (Yes/No): ")

        input_validation_yes_no = False

        while(input_validation_yes_no == False):
            if(again == "No" or again == "no"):
                play_again = False
                input_validation_yes_no = True
                print("Thanks for playing! You got " + str(user_score) +
                      " correct out of " + str(total_rolls) + " total dice rolls.")
            elif(again == "Yes" or again == "yes"):
                input_validation_yes_no = True
                continue
            else:
                print("Invalid input! Please enter yes or no.")
                again = input("Would you like to play again? (Yes/No): ")
