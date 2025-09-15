lista_de_compras = ["Tomate", "Arroz", "Feijão", "Batata", "Macarrão"]
opção = 0
while opção != 6:
    opção = int (input(f" Digite: \n 1-Atualizar \n 2-Remover \n 3-Excluir tudo \n 4-Ver lista de compra \n 5-Adicionar \n 6- Sair \n\n"))
    if opção == 1:
        antigo = (input(f" Item que deseja substituir: \n"))
    if antigo in lista_de_compras:
        novo = (input(f" Novo item: \n"))
        index = lista_de_compras.index(antigo)
        lista_de_compras[index]= novo 
        print (f" Lista atualizada:", lista_de_compras)
    elif opção == 2:
        compras = (input(f" O que você deseja remover? \n "))
        lista_de_compras.remove(compras)
        print (f" Item removido com sucesso! ")
    elif opção == 3:
        lista_de_compras.clear
        print (f" Lista de compras excluída com sucesso! ")
    elif opção == 4:
        print (f" Lista de compras {lista_de_compras}")
    elif opção == 5:
        compras = (input(f" O que você deseja adicionar na sua lista? \n "))
        lista_de_compras.append(compras)
        print (f" Item adicionado ")
    else:
        print (f" Obrigada pela presença, volte sempre! ")


        


