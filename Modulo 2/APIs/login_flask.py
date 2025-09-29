from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return '<h1> BEM VINDO </h1>'

@app.route('/nome')
def nome():
    nome = "Milena"
    return f'<h1> Nome: {nome} </h1>'

@app.route('/idade')
def idade ():
    idade = 23
    return f' <h1> Idade: {idade} </h1>'

if __name__ == "__main__":
    app.run(debug=True)