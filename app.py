__author__ = 'john'


from flask import Flask,make_response
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h2>Hello, World!</h2>"
@app.route('/greeting/<name>')
def greet(name):
    return make_response('<h1> Hello, %s! amakuru to murugo </h1>'%name)


@app.route('/counter/<int:number>')

def counter(number):
    numbers = ('zero','one','two','three','four','five')
    if number <= 5:
        return make_response('<h1> number %s!</h1>'%numbers[number])
    else:
        return make_response('<h1> the number is not in da range </h1>')
@app.route('/count/<int:value>')
def count(value):
    values = {1:'one',2:'two'}
    return make_response("Number %s"% values.get(value,'the number is no in the range'))

@app.route('/browser')
def req():
    user_agent = request.headers.get('User-Agent')
    return make_response('<p> Your browser is %s </p>'%user_agent)


if __name__ == '__main__':
    app.run(debug=True)