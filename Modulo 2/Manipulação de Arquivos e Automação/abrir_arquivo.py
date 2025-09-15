nome = (input(f" Digite o seu nome: \n"))
nota1 = float(input(f" Digite sua primeira nota: \n "))
nota2 = float(input(f" Digite sua segunda nota: \n "))
nota3 = float(input(f" Digite sua terceira nota: \n "))
media =(nota1 + nota2 + nota3/3)

with open (" nota.txt", "a" ) as notas:
   notas.write (nome +  "|" + f" {nota1} " + " | " + f" {nota2} " + " | " + f" {nota3}" + " | " + f"media: {media}  \n" )
