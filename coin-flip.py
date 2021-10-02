import random

play_again = True
user_score = 0
total_flips = 0
options = ['Heads', 'Tails']

while(play_again == True):
    heads_tails = random.randint(0, 1)
    if(total_flips == 0):
        print("Welcome to the coin toss game!")

    user_input = input("Please enter Heads or Tails (case sensitive!): ")
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
