import requests 
response = requests.get ("https://sp.senai.br/unidade/santanadeparnaiba/1")
status = response.status_code
if status <= 299 :
    print("Site encontrado, Status:",status)
else:
    print("Site não encontrado,Status:",status)
