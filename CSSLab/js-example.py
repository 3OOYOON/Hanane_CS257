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



if __name__ == '__main__':
    my_port = 5209
    app.run(host='0.0.0.0', port = my_port) 

