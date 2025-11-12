from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route ('/soma/<int:valor1>/<int:valor2>')
def somar(valor1, valor2):
    soma = valor1 + valor2
    return f'<h1> Resultado: {soma} <h1>'


@app.route('/subtração/<int:valor1>/<int:valor2>')
def subtrair(valor1, valor2):
    subtração = valor1 - valor2
    return f'<h1> Resultado: {subtração} <h1>'

@app.route('/multiplicação/<int:valor1>/<int:valor2>')
def multiplicar(valor1, valor2):
    multiplicação = valor1 * valor2
    return f'<h1> Resultado: {multiplicação} <h1>'

@app.route('/divisão/<int:valor1>/<int:valor2>')
def dividir(valor1 , valor2):
    if valor2 == 0:
        return f'<h1> Erro <h1>'
    divisão = valor1 / valor2
    return f'<h1> Resultado: {divisão} <h1>'


if __name__ == "__main__":
    app.run(debug=True)