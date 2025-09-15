kindle = ["Judas", "Corrupt", "Mendacium", "Os Setes Maridos De Evelyn Hugo", "Incipit "]
opçao = 0
while opçao != 5:
    opçao = int (input(f" Digite o que deseja fazer: \n 1- Ver livros lidos no kindle \n 2- Adiconar livros no kindle \n 3- Apagar livro do kindle \n 4- Modificar livro do kindle \n 5- Sair do kindle \n") )
    if opçao == 1:
        print (f" Livros lidos no kindle: {kindle} ")
    elif opçao == 2: 
        livros = (input(f" Qual livro você deseja adicionar no seu kindle? \n "))
        kindle.append (livros)
    elif opçao == 3:
        livros = (input (f" Qual livro voê deseja remover do seu kindle? \n "))
        kindle.remove(livros)
        print (f" livro removido com sucesso! ")
    elif opçao == 4:
        livros = (input (f" Qual livro voê deseja modificar? \n "))
        kindle[livros]
    else:
        print (f" saindo do sistema... ")
