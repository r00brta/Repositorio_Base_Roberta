#nome = input (f" Qual é o seu nome? ")
#altura = float (input (f" Qual é sua altura? ") )
#peso = float (input (f" Quanto você pesa? " ) )
#imc = peso/ (altura * altura )
opção = 3
while opção != 2: 
    opção = int (input (" Digite: \n 1- continuar no sistema \n 2- sair do sistema \n") )
    nome = (input (f" Qual é o seu nome? ") )
    altura = float (input (f" {nome} qual é sua altura? ") )
    peso = float (input (f" { nome} quanto você pesa? " ) )
    imc = peso/ (altura * altura )
    if imc <= 24.9:
        print (f" {nome} está com o peso normal ")
    elif imc >= 30.0:
        print (f" {nome} está sobrepeso ")
    else:
        print (f" {nome} está com obesidade grau I")

                    
