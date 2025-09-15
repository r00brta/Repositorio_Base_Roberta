nome = input (f" qual é o seu nome? " )
temperatura = float (input ( "qual é a temperatura de hoje? " ) )

if 20 <= temperatura <= 40:
    print (f"está quente")
elif 20 >= temperatura >= 5:
    print (f"está frio")
elif 0 <= temperatura <= 5:
    print (f"está gelado")
else:
    print (f"nois morre")
