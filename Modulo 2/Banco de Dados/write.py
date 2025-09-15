import csv
with open("dados.csv","a", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Honda","CG","2023","60000"])
