total = 0
média = 0 
maior = 0
for dia in range (1,6):
    participantes = int(input (f" Quantos participantes vieram no dia {dia}? \n ") )
    
    total += participantes
print (f" Total é: {total}")

média = total / 5

print (f" A média é: {média}")

if maior <= participantes:
    maior = participantes 
    print (f" Maior é: {maior}") 
