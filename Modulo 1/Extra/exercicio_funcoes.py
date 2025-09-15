def qual_livro ():
    livro = int (input (f" Qual livro você deseja ler? \n 1- Judas \n 2- Incipt \n 3- Devils Nigth \n 4- Desenfreados \n 5-Mendacium ") )
    if livro == 1:
        print (f" Òtima escolha!! ")
    elif livro == 2:
        print (f" Òtima escolha!! ")
    elif livro == 3:
        print (f" Òtima escolha!! ")
    elif livro == 4:
        print (f" Òtima escolha!! ")
    else:
        print (f" òtima escolha!! ")
def pessoa_para_ler ():
    pessoa = int (input (f" Com quem você desejar ler? \n 1- Isa feia \n 2- Mika linda \n") )
    if pessoa == 1:
        print (f" Tem certeza? Não é uma boa escolha!!!, mas qual ? ")
        qual_livro()
    else:
        print (f" Òtima escolha!!, mas qual ?? ")
        qual_livro()
opção = 0
while opção != 3:
    ler = int (input (f" Você deseja ler um livro? \n 1- Sim \n 2- Não \n 3- Sair \n") )
if ler == 1:
    pessoa_para_ler()
else: 
    print (f" Que pena, nos vemos na próxima ")

