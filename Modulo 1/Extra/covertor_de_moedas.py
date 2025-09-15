def convertor ():
    opção = 0
    while opção != 3:
            reais = 1
            dólar = 5.60
            opção = int (input (f" Digite:\n 1- Converter reais em dólar \n 2- converter dólar em reais \n 3- sair do sitema \n" ) )
    if opção == 1:
            valor = float (input (f" Digite um valor em reais: \n ") )
            resultado = valor / dólar
            print (f" US$ {resultado: .2f}")
    elif opção == 2:
            valor = float (input (f" Digite um valor em dólar: \n ") )
            resultado = valor * dólar
            print (f" R$ {resultado: .2f}")
    else:
            print (f" Siando do sistema... ")
convertor ()
    
