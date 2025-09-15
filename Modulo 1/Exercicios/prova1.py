Nome = (input (f" Qual é o nome do paciente? \n ") )
Peso = float(input (f" Digite o peso do(a) paciente: \n ") )
Altura = float (input (f" Digite a altura do(a) paciente: \n ") )
Imc = Peso/ (Altura * Altura)
if Imc <= 18.5:
    print (f" {Nome}, você está com o imc de {Imc} e abaixo do peso! ")
elif Imc <= 18.5 and 24.9:
    print (f" {Nome}, você está com o imc de {Imc} e com o peso normal! ")
elif Imc <= 25.0 and 29.9:
    print (f" {Nome}, você está com o imc de {Imc} e sobrepeso! ")
elif Imc <= 30.0 and 34.9:
    print (f" {Nome}, você está com o imc de {Imc} e com obesidade grau I! ")  
elif Imc <= 35.5 and 39.9:
    print (f" {Nome}, você está com o imc de {Imc} e com obesidade grau II! ")
else:
    print (f" {Nome}, você está com o imc de {Imc} e com obesidade grau III! ")
if Imc >= 30.0:
    print (f" Cuidado com a saúde! ")
else:
    (f" Está tudo ok! ")
