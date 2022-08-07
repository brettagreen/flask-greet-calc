from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def add_add():
    """adds two numbers."""
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(operations.add(a,b))

@app.route('/sub')
def sub_sub():
    """substracts attr b from attr a"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(operations.sub(a,b))

@app.route('/mult')
def mult_mult():
    """multiplies a by b"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(operations.mult(a,b))

@app.route('/div')
def div_div():
    """divides attr a by attr b"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(operations.div(a,b))

@app.route('/math/<op>')
def multi_math(op):
    math_map = {'add':operations.add, 'sub': operations.sub, 'mult':operations.mult, 'div':operations.div}
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(math_map[op](a,b))