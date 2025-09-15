import os 

#CRIAR PASTA 
#os.mkdir("Projetos")
#print("Pasta criada")

#CVRIAR ARQUIUVOS
#open("Projetos/matematica.txt", "w").close()
# open("Projetos/portugues.txt", "w").close()
# open("Projetos/ciências.txt", "w").close() 
# print ("arquivos criados")

#LISTAR ARQUIVOS
#arquivos = os.listdir("Projetos")
#for item in arquivos:
#    print(item)

#RENOEMANDO ARQUIVO 
#os.rename("projetos/portugues.txt", "projetos/história.txt")
#print("arquivo renomeado")

if os.path.exists("Projetos/matematica.txt"):
    os.remove("Projetos/matematica.txt")
    print("Arquivo apagado")
else:
    print("Arquivo não encontrado")
