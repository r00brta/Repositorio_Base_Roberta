numeroescolhido = int (input (f"digite o número que voce não sabe: " ) )
numeroinicio = int (input (f"digite o numero que voce quer iniciar: ") )
numerofim = int (input (f"digite o numero que vai terminar: ") )

numero = (numeroescolhido) 
for i in range ( numeroinicio,numerofim ):
    print (f" {i} x {numero} = {i * numero} ")
