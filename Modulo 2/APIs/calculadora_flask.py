from flask import Flask 

app = Flask(__name__)
@app.route('/')
def home():
    return '<h1> hello Flask </h1>'

@app.route('/soma')
def soma():
    n1= 7
    n2= 9
    soma = n1 + n2
    return f'<h1> Resultado: {soma} </h1>'

@app.route('/subtração')
def subtração():
    n1 = 25
    n2 = 10 
    subtração = n1 - n2
    return f'<h1> Resultado: {subtração} </h1>'

@app.route('/divisão')
def divisão():
    n1 = 65
    n2 = 10
    divisão = n1 / n2
    return f'<h1> Resultado: {divisão} </h1>'

@app.route('/multiplicação')
def multiplicação():
    n1 = 40
    n2 = 4
    multiplicação = n1 * n2
    return f'<h1> Resultado: {multiplicação} </h1>'

if __name__ == "__main__":
    app.run(debug=True)