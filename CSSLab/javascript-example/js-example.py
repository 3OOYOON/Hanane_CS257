from flask import Flask
from flask import render_template
import random
import psycopg2

app = Flask(__name__)


@app.route('/rps')
def welcome():
    message = "Welcome to My Example Webpage."
    message = message + " This text was produced by concatenating strings in Python!"
    return render_template("homepage.html", someText = message)


def fight(user_choice):
    potential_position = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(potential_position)

    if (computer_choice == 'Rock' and (user_choice == 'p' or user_choice == 'P')):
        print("Rock loses to Paper, you win!!!")
    elif (computer_choice == 'Paper' and (user_choice == 's' or user_choice == 'S')):
        print("Paper loses to Scissors, you win!!!")
    elif (computer_choice == 'Scissors' and (user_choice == 'r' or user_choice == 'R')):
        print("Scissors loses to Rock, you win!!!")
    elif computer_choice == user_choice.lower():
        print("It's a tie!")
    else:
        print("You lose")


def play_game():
    while True:
        user = input("Rock, Paper, or Scissors? You can just write r, p, or s: ")
        fight(user)
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            print("Thanks for playing!")
            break


if __name__ == '__main__':
    my_port = 5209
    app.run(host='0.0.0.0', port = my_port) 
