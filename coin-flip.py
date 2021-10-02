import random

heads_tails = random.randint(0, 1)
play_again = 1
user_score = 0
total_flips = 0
options = ['Heads', 'Tails']

while(play_again == 1):
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
    play_again = int(
        input("Would you like to play again? Please enter 1 for yes, or, 0 for no: "))
