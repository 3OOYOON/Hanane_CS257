from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index2.html")


# Lists of parts of speech
subjects = ['Alice', 'Alberto', 'Bob', 'Sara']
adjectives = ['wise', 'brave', 'curious', 'joyful']
verbs = ['sings', 'runs', 'jumps', 'reads']
places = ['in the park', 'at the library', 'on the mountain', 'near the lake']


def generate_sentence():
    subject = random.choice(subjects)
    adjective = random.choice(adjectives)
    verb = random.choice(verbs)
    place = random.choice(places)
    year = random.randint(1990, 2022)
    return sentance "{subject} the {adjective} {verb} {place} in {year}."


@app.route('/rand/sentence/gen')
def index():
    sentence = generate_sentence()
    return render_template('index2.html', sentence=sentence)

if __name__ == '__main__':
    my_port = 5209
    app.run(host='0.0.0.0', port = my_port)  
