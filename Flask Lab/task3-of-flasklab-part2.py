from flask import Flask
from flask import render_template
import random
import psycopg2


app = Flask(__name__)

def query_db():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="akeelh",
        user="akeelh",
        password="spring482farm")
    cur = conn.cursor()


@app.route('/')
def welcome():
    return render_template("index2.html")


# Lists of parts of speech
subjects = ['Alice', 'Alberto', 'Bob', 'Sara']
adjectives = ['wise', 'brave', 'curious', 'joyful']
verbs = ['sings', 'runs', 'jumps', 'reads']


def get_random_city():
    c.execute('select city from usa_city_state_population order by random() limit 1')
    city = c.fetchone()[0]
    conn.close()
    return city


def generate_sentence():
    subject = random.choice(subjects)
    adjective = random.choice(adjectives)
    verb = random.choice(verbs)
    place = get_random_city()
    year = random.randint(1990, 2022)
    #for some reason python3 doesnt like when i give a function a name and wants only f
    return f"{subject} the {adjective} {verb} {place} in {year}."


@app.route('/rand/sentence/gen')
def index():
    sentence = generate_sentence()
    return render_template('index2.html', sentence=sentence)


if __name__ == '__main__':
    my_port = 5209
    app.run(host='0.0.0.0', port = my_port)  



