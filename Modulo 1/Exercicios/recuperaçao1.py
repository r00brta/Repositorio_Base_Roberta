opção = "s"
print (f" Bem vindo ao nosso sistema! \n ")
while opção == "s":
    nome = (input (f" Qual é o seu nome? \n") )
    número = int (input (f" Digite um número inteiro: \n ") )
    if número % 2 == 0:
        print (f" {nome}, o número {número} escolhido é par! \n ")
    else:
        print (f" {nome}, o número {número} escolhido é ímpar! \n ")
    opção = (input (f" Deseja ver um novo número? \n S- sim \n N- não \n" ) )
    if opção == "n":
        print (f" Você saiu do sistema! \n Obrigada pela presença. ")

