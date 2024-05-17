from flask import Flask
from flask import render_template
import random
import psycopg2

app = Flask(__name__)


@app.route('/rps')
def welcome():
    message = """ Welcome to my Rock Paper Scissors Webpage.
    As you can guess you can play rock paper scissors on this site.
    Either press rock, paper, or scissors and see if you can beat the computer.
    You may either win, lose, or get in a tie."""
    return render_template("homepage.html", someText = message)



if __name__ == '__main__':
    my_port = 5209
    app.run(host='0.0.0.0', port = my_port) 

