import flask

app = flask.Flask(__name__)

#
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
    int(num1)
    int(num2)
    sum = num1 + num2;

    if Number.isInteger(num1) and Number.isInteger(num2):
        return '<h1 style="color:rgb(11, 11, 97)">' + sum + '</h1>'
    else:
        return '<h1 style="color:rgb(11, 11, 97)">' + "at least one of your inputs is not a number" + '</h1>'

if __name__ == '__main__':
    my_port = 5209
    app.run(host='0.0.0.0', port = my_port)
