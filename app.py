__author__ = 'john'


from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h2>Hello, World!</h2>"
@app.route('/greeting/<name>')
def greet(name):
    return '<h1> Hello, %s! amakuru to murugo </h1>'%name


@app.route('/counter/<int:number>')

def counter(number):
    numbers = ('zero','one','two','three','four','five')
    if number <= 5:
        return '<h1> number %s!</h1>'%numbers[number]
    else:
        return '<h1> the number is not in da range </h1>'
@app.route('/count/<int:value>')
def count(value):
    values = {1:'one',2:'two'}
    return "Number %s"% values.get(value,'the number is no in the range')


if __name__ == '__main__':
    app.run(debug=True)