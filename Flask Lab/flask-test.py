import flask
import psycopg2

app = flask.Flask(__name__)

def query_db():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="akeelh",
        user="akeelh",
        password="spring482farm")
    cur = conn.cursor()


@app.route('/hello')
def my_function():
    return "Hello World!"


@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string


@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:rgb(11, 11, 97)">' + word1 + '</h1>'


@app.route('/add/<num1>/<num2>')
def my_display2(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    sum = num1 + num2

    if isinstance(num1, int) and isinstance(num2, int):
        return '<h1 style="color:rgb(11, 11, 97)">' + str(sum) + '</h1>'
    else:
        return '<h1 style="color:rgb(11, 11, 97)">' + "at least one of your inputs is not a number " +'</h1>'
    

@app.route('/pop/<abbrev>')
def my_display3 (abbrev):
    abbrev = str(abbrev)

    if len(abbrev) == 2:
        cur.execute("select sum(population) from usa_city_state_population where state in (select state from usa_state_population where code = %s);", (state_name,))
    else:
        cur.execute("select sum(population) from usa_state_population where state = %s;", (state_name,))
    total_pop = cur.fetchone()[0]

    if isinstance(abbrev, str) and len(abbrev) == 2:
        return '<h1 style="color:rgb(11, 11, 97)">' + "The total population of " + str(abbrev) + "is "+ total_pop +'</h1>'

query_db()

if __name__ == '__main__':

    my_port = 5209
    app.run(host='0.0.0.0', port = my_port)


