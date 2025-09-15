import os 
import flet as ft

texto_pasta = ""
arquivo_criado = ""


def main(page: ft.Page):
    page.title ="Interface com OS"
    page.theme_mode = "DARK"
    page.bgcolor = "DARK"
    page.update()
    def criar_pasta(e):
        global texto_pasta
        texto_pasta = text_entrada.value
        try:
            os.mkdir(texto_pasta)
            resultado.value = f"Pasta criada: {texto_pasta}"
            resultado.color = "PINK"
            page.update()
        except FileExistsError:
            resultado.value = f"Não foi possível criar a pasta"
            
            
    def remover_pasta (e):
        try:
            nome_pasta = text_entrada.value
            os.rmdir(nome_pasta)
            resultado.value = f"Pasta Removida: {nome_pasta}"
            resultado.color = "PURPLE"
            page.update()
        except FileExistsError:
            resultado.value = f"Não foi possível remover a pasta"
            page.update()
            
    def criar_arquivo(e):
        global arquivo_criado
        global texto_pasta 
        arquivo_criado = text_entrada.value
        if texto_pasta == "":
                open(arquivo_criado,"w").close()
                resultado.value = f"Arquivo criado: {arquivo_criado}"
                resultado.value = f"Arquivo criado: {arquivo_criado}"
                resultado.color = "GREEN"
        else:
                open(f"{texto_pasta}/{arquivo_criado}","w").close()
                text_entrada.value = ""
                resultado.value = f"Arquivo criado: {arquivo_criado}"
                resultado.color = "GREEN"
        page.update()   
        resultado.value =f"Não foi possível criar o arquivo"
           
    def remover_arquivo(e):
        arquivo_removido = text_entrada.value
        if texto_pasta == "":
                os.remove(arquivo_criado)
                resultado.value = f"Arquivo Removido: {arquivo_removido}"
                resultado.color = "CYAN"
                page.update()
        else:
                os.remove(f"{texto_pasta}/{arquivo_criado}")
                resultado.value = f"Arquivo Removido: {arquivo_removido}"
                resultado.color = "CYAN"
                resultado.value = f"Não foi possível remover o arquivo"
                page.update()
          
    def renomear_arquivo(e):
        arquivo_novo = text_entrada.value
        try:
            os.rename(f"{texto_pasta}/{arquivo_criado}",f"{texto_pasta}/{arquivo_novo}")
            resultado.value = f"Arquivo renomeado para: {arquivo_novo}"
            resultado.color = "YELLOW"
        except FileExistsError:
            resultado.value = f"Não foi possível renomear o arquivo"
            page.update()
    
    

       
                        
    



    text_entrada =ft.TextField(label="Escreva algo...")
    botão_criar_pasta =ft.ElevatedButton("Criar pasta",on_click=criar_pasta,bgcolor="RED",color="DARK",width=400)
    botao_remover_pasta =ft.ElevatedButton("Remover pasta",on_click=remover_pasta,bgcolor="RED",color="DARK",width=400)
    botao_criar_arquivo =ft.ElevatedButton("Criar arquivo",on_click=criar_arquivo,bgcolor="GREY",color="WHITE",width=400)
    botao_remover_arquivo =ft.ElevatedButton("Remover arquivo",on_click=remover_arquivo,bgcolor="GREY",color="WHITE",width=400)
    botao_renomear_arquivo =ft.ElevatedButton("Renomear arquivo",on_click=renomear_arquivo,bgcolor="WHITE",color="RED",width=400)
    resultado = ft.Text("",size=40,color="GREY")

    page.add(
        ft.Row([text_entrada],alignment="center"),
        ft.Row([botão_criar_pasta, botao_remover_pasta,],alignment="center"),
        ft.Row([botao_criar_arquivo,botao_remover_arquivo],alignment="center"),
        ft.Row([botao_renomear_arquivo,],alignment="center"),
        ft.Row([resultado],alignment="center")
        )
ft.app(target=main)




#CRIAR PASTA 
#os.mkdir("Projetos")
#print("Pasta criada")

#CRIAR ARQUIVOS
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

#APAGAR ARQUIVO
# if os.path.exists("Projetos/matematica.txt"):
#     os.remove("Projetos/matematica.txt")
#     print("Arquivo apagado")
# else:
#     print("Arquivo não encontrado")
