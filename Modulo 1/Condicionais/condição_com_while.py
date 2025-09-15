opcao = 10
while opcao != 4:
    nome = (input (f" Qual é o seu nome? ") )
    opcao = int(input("digite : \n 1 - Pix \n 2- Deposito \n 3- Ver extrato \n 4- Sair do sitema \n"))

    if opcao == 1:
        nome = (input (f" Nome da pessoa:") )
        valor  = float (input (f" Quanto voce deseja pagar para {nome}? " ) )
        print(f" Voce pagou {valor} para {nome}" )
    elif opcao == 2:
        valor = float (input (f" Quanto voce deseja depositar? " ) )
        print (f" Voce depositou {valor} ")
    elif opcao == 3:
        saldo = (input (f"Deseja ver seu saldo ? ") )
        print (f" saldo indisponível" )
    else:
        print (f" Voce saiu do sistema ")

