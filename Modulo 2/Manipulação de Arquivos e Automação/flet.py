import flet as ft 

def main(page:ft.Page):
    page.theme_mode = "dark"
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.RED_500)
    texto_login = ft.Text("login:",size=60)
    entrada_texto_login = ft.TextField(width=600)
    texto_senha = ft.Text ("senha",size=60)
    entrada_texto_senha = ft.TextField(width=600,password=True,can_reveal_password=True)

    def click (e):
        valor_do_texto_login = texto_login.value
        print ("xD!",valor_do_texto_login)
    botao = ft.ElevatedButton("clique em mim",on_click=click)

    page.add(ft.Row([texto_login,entrada_texto_login]),
             ft.Row([texto_senha,entrada_texto_senha]),
             ft.Row([botao]))
    
ft.app(target=main)
