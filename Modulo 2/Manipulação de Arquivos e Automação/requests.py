import requests 

try:
    url = "https://sp.senai.br/unidade/santanadeparnaiba/"
    resposta = requests.get (url)
    status = resposta.status_code
    if status == 200:
         print("Site encontrado! Status:",status)
    else:
        print(f"Site não encontrado! Status:",status)


except:
    print (f"Algo deu errado")
